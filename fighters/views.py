from django.views.generic import TemplateView
from fighters.models import Cosmetic, Fighter
from hithub.utils import generate_signed_url
import requests
from django.core.files import File
from PIL import Image
from django.core.files.temp import NamedTemporaryFile
from fighters.utils import recolor_img

class FighterPageView(TemplateView):
    template_name = "fighters.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fighters = Fighter.objects.all()

        prepped_fighters = []

        for fighter in fighters:
            signed_cosmetics = []

            # Query the related cosmetics for the current fighter
            cosmetics_for_fighter = [
                fighter.cosmetic_base,
                fighter.cosmetic_hat,
                fighter.cosmetic_hair,
                fighter.cosmetic_eye,
                fighter.cosmetic_ear,
                fighter.cosmetic_beard,
                fighter.cosmetic_mouth,
                fighter.cosmetic_neck,
                fighter.cosmetic_body,
                fighter.cosmetic_arm,
                fighter.cosmetic_gloves,
                fighter.cosmetic_shorts,
                fighter.cosmetic_leg,
                fighter.cosmetic_feet,
                fighter.cosmetic_tattoo,
            ]

            # Generate signed URLs for the cosmetics
            for cosmetic in cosmetics_for_fighter:
                if cosmetic:
                    cosmetic_signed_url = generate_signed_url(cosmetic.img.name)

                    signed_cosmetics.append({
                        'cosmetic': cosmetic,
                        'signed_url': cosmetic_signed_url,
                    })

            prefix, suffix = "", ""
            if fighter.prefix is not None: prefix = fighter.prefix
            if fighter.suffix is not None: suffix = fighter.suffix
            fighter_name = f"{prefix} {fighter.name} {suffix}"
            prepped_fighters.append({
                'fighter': fighter,
                'name': fighter_name,
                'signed_cosmetics': signed_cosmetics,
            })

        context['prepped_fighters'] = prepped_fighters

        return context