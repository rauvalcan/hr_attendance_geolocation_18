/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { MyAttendances } from "@hr_attendance/components/my_attendances/my_attendances";
import { useService } from "@web/core/utils/hooks";

patch(MyAttendances.prototype, {
    setup() {
        super.setup(...arguments);
        this.notification = useService("notification");
        this.orm = useService("orm");
    },

    // Sobrescribimos la función de actualización de asistencia
    async updateAttendance() {
        // Obtenemos la ubicación antes de llamar al servidor
        try {
            const position = await this.getGeolocation();
            const context = {
                latitude: position.coords.latitude,
                longitude: position.coords.longitude,
            };

            // Llamamos al método original de Odoo, pero con el contexto enriquecido
            await this.orm.call(
                "hr.employee",
                "attendance_manual",
                [[this.employee.id], "hr_attendance.hr_attendance_action_my_attendances"],
                { context }
            );
            this.notification.add("Ubicación registrada.", { type: "success" });
            // Actualizamos el componente para reflejar el cambio
            this.props.update();
            
        } catch (error) {
            // Si hay un error (p. ej., el usuario deniega la ubicación), lo notificamos
            console.error(error.message);
            this.notification.add(error.message, { type: "danger" });
        }
    },

    /**
     * Obtiene la geolocalización del navegador.
     * Devuelve una Promesa que se resuelve con la posición o se rechaza con un error.
     * @returns {Promise<GeolocationPosition>}
     */
    getGeolocation() {
        return new Promise((resolve, reject) => {
            if (!("geolocation" in navigator)) {
                reject(new Error("Tu navegador no soporta geolocalización."));
                return;
            }
            navigator.geolocation.getCurrentPosition(
                (position) => resolve(position),
                (error) => {
                    let message = "No se pudo obtener la ubicación. ";
                    if (error.code === 1) { // PERMISSION_DENIED
                        message += "Por favor, permite el acceso a la ubicación en tu navegador.";
                    }
                    reject(new Error(message));
                }
            );
        });
    }
});