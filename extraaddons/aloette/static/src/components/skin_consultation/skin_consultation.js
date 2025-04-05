/** @odoo-module **/

import {registry} from '@web/core/registry';
import { Component } from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";


export class SkinConsultation extends Component {
    // static template = 'aloette.SkinConsultation';
    // static props = {};

    setup() {
        this.orm = useService('orm');
        this.notification = useService('notification');
        this.rpc = useService('rpc')

        this.state = {
            likes: [],
            improvements: [],
            vascularity: null,
            skinTexture: null,
            pigmentation: null,
            hydration: null,
            sebaceousActivity: null
        };

        this.skinAttributes = [
            { id: 1, name: 'Texture' },
            { id: 2, name: 'Complexion' },
            { id: 3, name: 'Moisture Content' },
            { id: 4, name: 'Other' }
        ];

        this.vascularityOptions = [
            { id: 1, name: 'Hypo' },
            { id: 2, name: 'Normal' },
            { id: 3, name: 'Hyper' },
            { id: 4, name: 'Other' }
        ];

        this.skinTextureOptions = [
            { id: 1, name: 'Thin' },
            { id: 2, name: 'Medium' },
            { id: 3, name: 'Thick' },
            { id: 4, name: 'Other' }
        ];

        this.depthOfPigmentationOptions = [
            { id: 1, name: 'Superficial' },
            { id: 2, name: 'Dermal' },
            { id: 3, name: 'Both' },
            { id: 4, name: 'Other' }
        ];

        this.hydrationLevelOptions = [
            { id: 1, name: 'Extreme Dehydrated' },
            { id: 2, name: 'Dehydrated' },
            { id: 3, name: 'Normal' },
            { id: 4, name: 'Other' }
        ];

        this.sebaceousActivityOptions = [
            { id: 1, name: 'Hypo' },
            { id: 2, name: 'Normal' },
            { id: 3, name: 'Hyper' },
            { id: 4, name: 'Other' }
        ];

        // Add similar options for other categories
    }

    updateLikes(attributeId, checked) {
        if (checked) {
            if (this.state.likes.length < 3) {
                this.state.likes.push(attributeId);
            }
        } else {
            this.state.likes = this.state.likes.filter(id => id !== attributeId);
        }
    }

    updateImprovements(attributeId, checked) {
        if (checked) {
            if (this.state.improvements.length < 3) {
                this.state.improvements.push(attributeId);
            }
        } else {
            this.state.improvements = this.state.improvements.filter(id => id !== attributeId);
        }
    }

    updateVascularity(optionId) {
        this.state.vascularity = optionId;
    }

    updateSkinTexture(optionId) {
        this.state.skinTexture = optionId;
    }

    updatePigmentation(optionId) {
        this.state.pigmentation = optionId;
    }

    updateHydration(optionId) {
        this.state.hydration = optionId;
    }

    updateSebaceousActivity(optionId) {
        this.state.sebaceousActivity = optionId;
    }

    // Check if fields are not empty
    isFormValid() {
        return (
            this.state.likes.length > 0 &&
            this.state.improvements.length > 0 &&
            this.state.vascularity !== undefined &&
            this.state.skinTexture !== undefined &&
            this.state.pigmentation !== undefined &&
            this.state.hydration !== undefined &&
            this.state.sebaceousActivity !== undefined
        );
    }



    async onSubmit() {
        if (!this.isFormValid()) {
            this.notification.add("Please fill in all fields before submitting", { type: 'danger' });
            return;
        }

        // Map IDs to names for likes
        const likeNames = this.state.likes.map(id => 
            this.skinAttributes.find(attr => attr.id === id)?.name.toLowerCase()
        );

        // Map IDs to names for improvements
        const improvementNames = this.state.improvements.map(id => 
            this.skinAttributes.find(attr => attr.id === id)?.name.toLowerCase()
        );

        // Map IDs to names for other fields
        const vascularityName = this.vascularityOptions.find(opt => opt.id === this.state.vascularity)?.name.toLowerCase();
        const skinTextureName = this.skinTextureOptions.find(opt => opt.id === this.state.skinTexture)?.name.toLowerCase();
        const pigmentationName = this.depthOfPigmentationOptions.find(opt => opt.id === this.state.pigmentation)?.name.toLowerCase();
        const hydrationName = this.hydrationLevelOptions.find(opt => opt.id === this.state.hydration)?.name.toLowerCase();
        const sebaceousActivityName = this.sebaceousActivityOptions.find(opt => opt.id === this.state.sebaceousActivity)?.name.toLowerCase();

        console.log('Like Names:', likeNames);
        console.log('Improvement Names:', improvementNames);
        console.log('Vascularity Name:', vascularityName);
        console.log('Skin Texture Name:', skinTextureName);
        console.log('Pigmentation Name:', pigmentationName);
        console.log('Hydration Name:', hydrationName);
        console.log('Sebaceous Activity Name:', sebaceousActivityName);

        try {
            const result = await this.orm.create("skin.consultation", [{
                like_about_skin: JSON.stringify(likeNames),
                improve_about_skin: JSON.stringify(improvementNames),
                vascularity: vascularityName,
                skin_texture: skinTextureName,
                pigmentation: pigmentationName,
                hydration: hydrationName,
                sebaceous_activity: sebaceousActivityName
            }]);
            
            this.notification.add("Consultation submitted successfully!", { type: 'success' });
            return result;
        } catch (error) {
            this.notification.add(error, { type: 'danger' });
            this.notification.add("Failed to submit consultation", { type: 'danger' });
        }
    }
}

SkinConsultation.template = 'aloette.SkinConsultation';
registry.category("actions").add("aloette.SkinConsultation", SkinConsultation);
