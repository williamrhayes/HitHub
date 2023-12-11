from django.db import models
from django.db.models import F

# Create your models here.
# Create your models here.
class Fighter(models.Model):
    # Establish Biographical Features
    date_of_birth = models.DateTimeField(auto_now_add=True)
    prefix = models.CharField(max_length=256, null=False)
    name = models.CharField(max_length=256, null=False)
    suffix = models.CharField(max_length=256, null=False)
    title = models.CharField(f"{F('prefix')} {F('name')} {F('suffix')}",
                             output_field=models.CharField(),
                             db_persist=True)
    bio = models.CharField(max_length=2048, null=True)

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
    stance = models.TextChoices(['Orthodox', 'Switch', 'Southpaw', 'Open Stance', 'Sideways', 'Illegal'], null=False)
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
    strikes_per_second = models.CharField(F('total_fight_time'),
                             output_field=models.FloatField(),
                             db_persist=True)
    submissions_per_second = models.CharField(F('total_fight_time'),
                             output_field=models.FloatField(),
                             db_persist=True)
    takedowns_per_second = models.CharField(F('total_fight_time'),
                             output_field=models.FloatField(),
                             db_persist=True)
    movements_per_second = models.CharField(F('total_fight_time'),
                             output_field=models.FloatField(),
                             db_persist=True)
    knock_downs = models.IntegerField(null=False)
    #strike_victories; Not sure how to implement this one yet

    def __str__(self):
        return self.title