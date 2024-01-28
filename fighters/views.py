from django.views.generic import TemplateView
from fighters.models import Cosmetic, Fighter
from hithub.utils import generate_signed_url

class FighterPageView(TemplateView):
    template_name = "fighters.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Query the cosmetics related to fighters or adjust the query based on your model structure
        cosmetics = Cosmetic.objects.all()
        
        # Query the cosmetics related to fighters or adjust the query based on your model structure
        # Generate signed URLs for cosmetics and pass them to the template
        signed_cosmetics = []
        for cosmetic in cosmetics:
            signed_url = generate_signed_url(cosmetic.img.name)  # Assuming img is the field name
            signed_cosmetics.append({
                'cosmetic': cosmetic,
                'signed_url': signed_url,
            })

        context['cosmetics'] = signed_cosmetics # Pass the cosmetics to the template
        context['fighters'] = Fighter.objects.all()  # Pass the fighters to the template
        
        return context