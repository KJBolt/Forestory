/** @odoo-module */

import { isMobileOS } from "@web/core/browser/feature_detection";
import { useService } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";
import { ListRenderer } from "@web/views/list/list_renderer";
import { PromoteStudioDialog } from "@ofy_web_responsive/webclient/promote_studio_dialog/promote_studio_dialog";
import { useState, onWillUnmount } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";

export const patchListRendererDesktop = () => ({
    setup() {
        super.setup(...arguments);
        this.userService = useService("user");
        this.actionService = useService("action");
        const list = this.props.list;

        const { actionId, actionType } = this.env.config || {};

        // Start by determining if the current ListRenderer is in a context that would
        // allow the edition of the arch by studio.
        // It needs to be a full list view, in an action
        // (not a X2Many list, and not an "embedded" list in another component)
        const isPotentiallyEditable =
            !isMobileOS() &&
            this.userService.isSystem &&
            list === list.model.root &&
            actionId &&
            actionType === "ir.actions.act_window";
        this.studioEditable = useState({ value: isPotentiallyEditable });

        if (isPotentiallyEditable) {
            const computeStudioEditable = () => {
                // Finalize the computation when the actionService is ready.
                // The following code is copied from studioService.
                const action = this.actionService.currentController.action;
                if (!action.xml_id) {
                    return false;
                }
                if (
                    action.res_model.indexOf("settings") > -1 &&
                    action.res_model.indexOf("x_") !== 0
                ) {
                    return false; // settings views aren't editable; but x_settings is
                }
                if (action.res_model === "board.board") {
                    return false; // dashboard isn't editable
                }
                if (action.view_mode === "qweb") {
                    // Apparently there is a QWebView that allows to
                    // implement ActWindow actions that are completely custom
                    // but not editable by studio
                    return false;
                }
                if (action.res_model === "knowledge.article") {
                    // The knowledge form view is very specific and custom, it doesn't make sense
                    // to edit it. Editing the list and kanban is more debatable, but for simplicity's sake
                    // we set them to not editable too.
                    return false;
                }
                return Boolean(action.res_model);
            };
            const onUiUpdated = () => {
                this.studioEditable.value = computeStudioEditable();
            };
            this.env.bus.addEventListener("ACTION_MANAGER:UI-UPDATED", onUiUpdated);
            // Stop Listening to "ACTION_MANAGER:UI-UPDATED"
            onWillUnmount(() => {
                this.env.bus.removeEventListener("ACTION_MANAGER:UI-UPDATED", onUiUpdated);
            });
        }
    },

    get isStudioEditable() {
        return this.studioEditable.value;
    },

    set isStudioEditable(value) {
        this.studioEditable.value = value;
    },

    get displayOptionalFields() {
        return this.isStudioEditable || super.displayOptionalFields;
    },

    /**
     * This function opens promote studio dialog
     *
     * @private
     */
    onSelectedAddCustomField() {
        this.env.services.dialog.add(PromoteStudioDialog, {
            title: _t("Odoo Studio - Add new fields to any view"),
        });
    },
});

export const unpatchListRendererDesktop = patch(ListRenderer.prototype, patchListRendererDesktop());
