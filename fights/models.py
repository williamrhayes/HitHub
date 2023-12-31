from django.db import models
from fighters.models import Fighter

# The high-level results of a fight
class Fight(models.Model):
    # Select the two fighters who are participating
    fighter_a_id = models.ForeignKey(Fighter, on_delete=models.CASCADE, limit_choices_to={"is_retired": False, "is_deceased": False, "is_enlightened": False, "is_exiled": False, "is_banished": False,}, null=False, related_name='fights_as_fighter_a')
    fighter_b_id = models.ForeignKey(Fighter, on_delete=models.CASCADE, limit_choices_to={"is_retired": False, "is_deceased": False, "is_enlightened": False, "is_exiled": False, "is_banished": False,}, null=False, related_name='fights_as_fighter_b')

    # Winning Fighter, this will be determined at the outset of the fight
    winning_fighter_id = models.IntegerField(blank=True, null=True)
    final_round = models.IntegerField(blank=True, null=True)
    victory_type = models.CharField(default='DI', choices={'DI': 'Distance', 'KO': 'Knockout', 'SU': 'Submission', 'XX': 'Death', 'NC': 'No Contest'}, max_length=2)

    # Establish Biographical Features
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.fighter_a_id} vs {self.fighter_b_id}"

# Details of the fight (Actual moves used in what sequence)
class FightDetail(models.Model):
    fight_id = models.ForeignKey(Fight, on_delete=models.CASCADE, null=False, related_name='fightdetails')
    is_successful=models.BooleanField(null=False)
    aggressor=models.ForeignKey(Fight, on_delete=models.CASCADE, null=False, related_name='fightdetails_as_aggressor')
    defender=models.ForeignKey(Fight, on_delete=models.CASCADE, null=False, related_name='fightdetails_as_defender')
    action_attempted=models.CharField(null=False, default='NA', choices={'NA': 'No Action', "AT": "Attack", "TD": "Takedown Attempt", "RV": "Reversal Attempt", "BA": "Breakaway Attempt"}, max_length=2)
    sub_action_attempted=models.CharField(blank=True, null=True, max_length=32)
    aggressor_position=models.CharField(choices={'W': 'Victory', 'L': "Defeat", 'DG': 'Dominant Ground','UG': 'Unsecure Ground', 'VG': 'Vulnerable Ground', 'CL': 'Clinch', 'DI': 'Distance'}, blank=True, null=True, max_length=2)
    action_details=models.CharField(blank=True, null=True, max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    step_number = models.IntegerField()

    # Automatically order by step_number when querying the
    # Fight Details
    class Meta:
        ordering = ['step_number']

    def __str__(self) -> str:
        return f"{self.step_number}: {self.aggressor} used {self.action_attempted}"

class UpcomingFight(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    fighter_a_id = models.ForeignKey(Fighter, on_delete=models.CASCADE, limit_choices_to={"is_retired": False, "is_deceased": False, "is_enlightened": False, "is_exiled": False, "is_banished": False,}, null=False, related_name='upcoming_fights_as_fighter_a')
    fighter_b_id = models.ForeignKey(Fighter, on_delete=models.CASCADE, limit_choices_to={"is_retired": False, "is_deceased": False, "is_enlightened": False, "is_exiled": False, "is_banished": False,}, null=False, related_name='upcoming_fights_as_fighter_b')

    def __str__(self) -> str:
        return f"{self.fighter_a_id} vs {self.fighter_b_id}"