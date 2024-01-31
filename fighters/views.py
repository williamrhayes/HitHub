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
                    color_data = cosmetic.color_data
                    cosmetic_signed_url = generate_signed_url(cosmetic.img.name)  # Assuming img is the field name
                    #img = self.extract_img(cosmetic_signed_url, color_data)

                    #altered_img.show()

                    signed_cosmetics.append({
                        'cosmetic': cosmetic,
                        'signed_url': cosmetic_signed_url,
                        #'img': img,
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
    
    def extract_img(self, cosmetic_signed_url, color_data):
        response = requests.get(cosmetic_signed_url)
        if response.status_code == 200:
            with NamedTemporaryFile() as temp_image_file:
                temp_image_file.write(response.content)
                temp_image_file.flush()

                # Open the downloaded image using PIL
                with Image.open(temp_image_file.name) as pil_image:
                    # Apply your recoloring function
                    img = pil_image.convert("RGBA")
                    # If the color is re-defined as color shifted in
                    # the color metadata, apply the re-coloring function.
                    if color_data["is_color_shifted"]:
                        return (recolor_img(img, new_base_color=color_data["new_base_color"], 
                                                constant_colors=color_data["constant_colors"], 
                                                independent_colors=color_data["independent_colors"]))
                    return img