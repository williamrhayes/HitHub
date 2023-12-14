from django.db import models
from django.db.models import F
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Fighter(models.Model):
    # Establish Biographical Features
    date_of_birth = models.DateTimeField(auto_now_add=True)
    prefix = models.CharField(max_length=256, null=False)
    name = models.CharField(max_length=256, null=False)
    suffix = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=2048, null=True)

    # Establish Cosmetics that Fighter has Equipped
    cosmetic_hair = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "HAIR"}, null=True, related_name='fighters_hair')
    cosmetic_eye = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "EYE"}, null=True, related_name='fighters_eye')
    cosmetic_ear = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "EAR"}, null=True, related_name='fighters_ear')
    cosmetic_beard = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "BEARD"}, null=True, related_name='fighters_beard')
    cosmetic_mouth = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "MOUTH"}, null=True, related_name='fighters_mouth')
    cosmetic_neck = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "NECK"}, null=True, related_name='fighters_neck')
    cosmetic_body = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "BODY"}, null=True, related_name='fighters_body')
    cosmetic_arm = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "ARM"}, null=True, related_name='fighters_arm')
    cosmetic_gloves = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "GLOVES"}, null=True, related_name='fighters_gloves')
    cosmetic_shorts = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "SHORTS"}, null=True, related_name='fighters_shorts')
    cosmetic_leg = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "LEG"}, null=True, related_name='fighters_leg')
    cosmetic_feet = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "FEET"}, null=True, related_name='fighters_feet')
    cosmetic_tattoo = models.ForeignKey('Cosmetic', blank=True, on_delete=models.CASCADE, limit_choices_to={"type": "TATTOO"}, null=True, related_name='fighters_tattoo')

    # Establish Lifestyle Features
    is_athiest = models.BooleanField(null=False)
    is_abstinent = models.BooleanField(null=False)
    is_badboy = models.BooleanField(null=False)
    is_derranged = models.BooleanField(null=False)
    is_offensive = models.BooleanField(null=False)
    is_radioactive = models.BooleanField(null=False)
    is_infected = models.BooleanField(default=False, null=False)
    is_injured = models.BooleanField(default=False, null=False)
    is_intoxicated = models.BooleanField(default=False, null=False)
    is_incarcerated = models.BooleanField(default=False, null=False)
    is_enlightened = models.BooleanField(default=False, null=False)
    is_banished = models.BooleanField(default=False, null=False)
    is_exiled = models.BooleanField(default=False, null=False)
    is_retired = models.BooleanField(default=False, null=False)
    is_deceased = models.BooleanField(default=False, null=False)

    # Establish Trainable Features
    has_visited_ancient_temple = models.BooleanField(default=False, null=True)
    has_monastic_training = models.BooleanField(default=False, null=True)
    is_roastmaster = models.BooleanField(default=False, null=True)
    is_rehabilitated = models.BooleanField(default=False, null=True)

    # Establish Fighter Stats
    height = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    reach = models.IntegerField(null=False)
    stance = models.CharField(default='OR', choices={'OR': 'Orthodox', 'SW': 'Switch', 'SP': 'Southpaw', 'OS':'Open Stance', 'SW': 'Sideways', 'KY': 'Kentucky', 'IL': 'Illegal'}, max_length=2)
    
    # It makes the most sense to just store this information as
    # an accessible JSON object. That way, whenever we want to 
    # retrieve information about a fighter we can retrieve it once
    # and don't have to keep calling the database
    stats = models.JSONField(default=dict, null=False)

    def __str__(self):
        return f"{self.prefix} {self.name} {self.suffix}"
    
# Wearable cosmetics for the fighter
class Cosmetic(models.Model):
    name = models.CharField(max_length=32, null=False)

    # Establish Biographical Features
    cosmetic_choices = {
        "HAIR": "Hair",
        "EYE": "Eyes",
        "EAR": "Ears",
        "BEARD": "Beard",
        "MOUTH": "Mouth",
        "NECK": "Neck",
        "BODY": "Body",
        "ARM": "Arms",
        "GLOVES": "Gloves",
        "SHORTS": "Shorts",
        "LEG": "Legs",
        "FEET": "Feet",
        "TATTOO": "Tattoos",
    }
    type = models.CharField(max_length=8, choices=cosmetic_choices, null=False)

    # Rarity follows the CRUEL system (common, rare, uncommon, exotic, legendary)
    rarity_choices = {
        "C": "Common",
        "U": "Uncommon",
        "R": "Rare",
        "E": "Exotic",
        "L": "Legendary",
    }
    rarity = models.CharField(default="C", max_length=1, choices=rarity_choices, null=False)

    # Primary colors of the object in question. This can be found programatically and will
    # follow the format of R_G_B_A
    primary_color = models.CharField(blank=True, max_length=16, null=True)
    secondary_color = models.CharField(blank=True, max_length=16, null=True)
    tertiary_color = models.CharField(blank=True, max_length=16, null=True)

    # Color shift of cosmetic (could be useful for painting later on)
    color_shift_r = models.IntegerField(default=0,  null=False, validators=[MinValueValidator(0),MaxValueValidator(255)])
    color_shift_g = models.IntegerField(default=0,  null=False, validators=[MinValueValidator(0),MaxValueValidator(255)])
    color_shift_b = models.IntegerField(default=0,  null=False, validators=[MinValueValidator(0),MaxValueValidator(255)])

    # Load in the image of the cosmetic
    img = models.ImageField(null=False)

    # Load in the metadata of the cosmetic
    metadata = models.JSONField(null=True)

    def __str__(self):
        return self.name