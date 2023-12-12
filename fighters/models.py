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
    title = models.CharField(f"{F('prefix')} {F('name')} {F('suffix')}", max_length=768)
    bio = models.CharField(max_length=2048, null=True)

    # Establish Cosmetics that Fighter has Equipped
    cosmetic_hair = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "HAIR"}, null=True, related_name='fighters_hair')
    cosmetic_eye = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "EYE"}, null=True, related_name='fighters_eye')
    cosmetic_ear = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "EAR"}, null=True, related_name='fighters_ear')
    cosmetic_beard = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "BEARD"}, null=True, related_name='fighters_beard')
    cosmetic_mouth = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "MOUTH"}, null=True, related_name='fighters_mouth')
    cosmetic_neck = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "NECK"}, null=True, related_name='fighters_neck')
    cosmetic_body = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "BODY"}, null=True, related_name='fighters_body')
    cosmetic_arm = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "ARM"}, null=True, related_name='fighters_arm')
    cosmetic_gloves = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "GLOVES"}, null=True, related_name='fighters_gloves')
    cosmetic_shorts = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "SHORTS"}, null=True, related_name='fighters_shorts')
    cosmetic_leg = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "LEG"}, null=True, related_name='fighters_leg')
    cosmetic_feet = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "FEET"}, null=True, related_name='fighters_feet')
    cosmetic_tattoo = models.ForeignKey('Cosmetic', on_delete=models.CASCADE, limit_choices_to={"type": "TATTOO"}, null=True, related_name='fighters_tattoo')

    # Establish Lifestyle Features
    is_athiest = models.BooleanField(null=False)
    is_abstinent = models.BooleanField(null=False)
    is_badboy = models.BooleanField(null=False)
    is_derranged = models.BooleanField(null=False)
    is_radioactive = models.BooleanField(null=False)
    is_offensive = models.BooleanField(null=False)
    is_on_drugs = models.BooleanField(default=False, null=False)
    is_infected = models.BooleanField(default=False, null=False)
    is_injured = models.BooleanField(default=False, null=False)
    is_retired = models.BooleanField(default=False, null=False)
    is_deceased = models.BooleanField(default=False, null=False)

    # Establish Trainable Features
    has_visited_ancient_temple = models.BooleanField(default=False, null=True)
    has_monastic_training = models.BooleanField(default=False, null=True)
    is_roastmaster = models.BooleanField(default=False, null=True)

    # Establish Fighter Stats
    height = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    reach = models.IntegerField(null=False)
    stance = models.CharField(default='OR', choices={'OR': 'Orthodox', 'SW': 'Switch', 'SP': 'Southpaw', 'OS':'Open Stance', 'SW': 'Sideways', 'IL': 'Illegal'}, max_length=2)
    strike_attempt_successes = models.IntegerField(null=False)
    strike_attempt_failures = models.IntegerField(null=False)
    strike_defense_successes = models.IntegerField(null=False)
    strike_defense_failures = models.IntegerField(null=False)
    sig_strike_attempt_successes = models.IntegerField(null=False)
    sig_strike_attempt_failures = models.IntegerField(null=False)
    head_strike_attempts = models.IntegerField(null=False)
    body_strike_attempts = models.IntegerField(null=False)
    leg_strike_attempts = models.IntegerField(null=False)
    takedown_attempt_successes = models.IntegerField(null=False)
    takedown_attempt_failures = models.IntegerField(null=False)
    takedown_defense_successes = models.IntegerField(null=False)
    takedown_defense_failures = models.IntegerField(null=False)
    submission_attempt_successes = models.IntegerField(null=False)
    submission_attempt_failures = models.IntegerField(null=False)
    submission_defense_successes = models.IntegerField(null=False)
    submission_defense_failures = models.IntegerField(null=False)
    control_time_success = models.IntegerField(null=False)
    control_time_failure = models.IntegerField(null=False)
    total_fight_time = models.FloatField(null=False)
    knock_downs = models.IntegerField(null=False)
    #strikes_per_second = models.FloatField(F('total_fight_time') / F('total_fight_time'),
    #                         output_field=models.FloatField(),
    #                         db_persist=True)
    #submissions_per_second = models.FloatField(F('total_fight_time') / F('total_fight_time'),
    #                         output_field=models.FloatField(),
    #                         db_persist=True)
    #takedowns_per_second = models.FloatField(F('total_fight_time'),
    #                         output_field=models.FloatField(),
    #                         db_persist=True)
    #movements_per_second = models.FloatField(F('total_fight_time'),
    #                         output_field=models.FloatField(),
    #                         db_persist=True)
    #strike_victories; Not sure how to implement this one yet

    def __str__(self):
        return self.title
    
# Wearable cosmetics for the fighter
class Cosmetic(models.Model):
    name = models.CharField(max_length=32, null=False)

    # Establish Biographical Features
    cosmetic_choices = {
        "HAIR": "HAIR",
        "EYE": "EYE",
        "EAR": "EAR",
        "BEARD": "BEARD",
        "MOUTH": "MOUTH",
        "NECK": "NECK",
        "BODY": "BODY",
        "ARM": "ARM",
        "GLOVES": "GLOVES",
        "SHORTS": "SHORTS",
        "LEG": "LEG",
        "FEET": "FEET",
        "TATTOO": "TATTOO",
    }
    type = models.CharField(max_length=8, choices=cosmetic_choices, null=False)

    # Rarity follows the CRUEL system (common, rare, uncommon, exotic, legendary)
    rarity_choices = {
        "C": "COMMON",
        "U": "UNCOMMON",
        "R": "RARE",
        "E": "EXOTIC",
        "L": "LEGENDARY",
    }
    rarity = models.CharField(default="C", max_length=1, choices=rarity_choices, null=False)

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