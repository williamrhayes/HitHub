from django.db import models
from django.conf import settings
from fighters.models import Fighter
from fights.models import UpcomingFight

# Base bet class. All other bets must include this information
# and therefore will inherit from this class.
class Bet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    placed_on = models.DateTimeField(auto_now_add=True)
    
    class BetStatus(models.TextChoices):
        WON = 'W', 'Won'
        LOST = 'L', 'Lost'
        PENDING = 'P', 'Pending'
        RETURNED = 'R', 'Returned'
    status = models.CharField(max_length=1, choices=BetStatus.choices, default=BetStatus.PENDING)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user} Bet {self.placed_on}"

# Moneyline bets - Betting on which fighter will win
class MoneylineBet(Bet):
    bet_type = "moneyline"
    fight = models.ForeignKey(UpcomingFight, related_name='moneyline_bets', on_delete=models.CASCADE)
    chosen_fighter = models.ForeignKey(Fighter, related_name='chosen_for_moneyline', on_delete=models.CASCADE)
    odds = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Moneyline bet on {self.chosen_fighter} by {self.user}"
    
# Totals bets - Betting on how long the fight will last
class TotalsBet(Bet):
    bet_type = "totals"
    fight = models.ForeignKey(UpcomingFight, related_name='totals_bets', on_delete=models.CASCADE)
    odds = models.DecimalField(max_digits=5, decimal_places=2)
    num_rounds = models.IntegerField(
        choices=[(1, "1.5 Rounds"), 
                 (2, "2.5 Rounds"), 
                 (3, "3.5 Rounds"), 
                 (4, "4.5 Rounds")])
    
    class OverUnder(models.TextChoices):
        OVER = 'O', 'Over'
        UNDER = 'U', 'Under'
    
    over_or_under = models.CharField(max_length=1, choices=OverUnder.choices)

    def __str__(self):
        return f"Totals bet on {self.fight} by {self.user}"
