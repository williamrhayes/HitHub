from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from fighters.models import SpiritFighter, Fighter, Cosmetic, Name  # Import the Fighter model from the "fighters" app
import random
import numpy as np

# Create a new fighter when an account is created
@receiver(post_save, sender=CustomUser)
def create_fighter(sender, instance, created, **kwargs):
    fighter_data = {}
    if created:
        # The user who is created will automatically sponsor the new fighter.
        fighter_data["sponsor"] = instance.id
        # Create a new fighter;
        # Determine the rarity of the fighter 
        rarity_char, rarity_num = determine_rarity()
        fighter_data["rarity"] = rarity_char
        # Select a Spirit Fighter based on this rarity
        spirit_fighter = determine_spirit_fighter()

        # Determine the fighter's name based on the rarity
        prefix, suffix, name = determine_fighter_name(rarity_char=rarity_char)
        fighter_data["prefix"] = prefix
        fighter_data["name"] = name
        fighter_data["suffix"] = suffix
        # Determine the fighter's Cosmetics

        # Determine the fighter's Spirit Fighter


        Fighter.objects.create(**fighter_data)

# Determine the rarity of the fighter
def determine_rarity():
    rank_rarities = {"C": 1, "U": 1/4, "R": 1/32, "E": 1/256, "L": 1/2048}
    rando = np.random.uniform()
    if rando < rank_rarities["L"]: return "L", 5
    if rando < rank_rarities["E"]: return "E", 4
    if rando < rank_rarities["R"]: return "R", 3
    if rando < rank_rarities["U"]: return "U", 2
    return "C", 1

# Determine the spirit fighter associated with our fighter,
# along with that fighter's height, weight, stance, and overall stats
def determine_spirit_fighter(rarity_char):
    spirit_fighters = SpiritFighter.objects.all()
    log_total_fights_dict = {}
    for fighter in spirit_fighters:
        total_fights = fighter.w + fighter.l + fighter.d
        log_total_fights_dict[fighter.id] = np.log(total_fights)

    log_mean_fights = np.array(list(log_total_fights_dict.values())).mean()
    log_stdev_fights = np.array(list(log_total_fights_dict.values())).std()

    spirit_fighter_rarities = {
        "C": int(np.e**(log_mean_fights)),
        "U": int(np.e**(log_mean_fights + (1 * log_stdev_fights))),
        "R": int(np.e**(log_mean_fights + (1.4 * log_stdev_fights))),
        "E": int(np.e**(log_mean_fights + (1.75 * log_stdev_fights))),
        "L": int(np.e**(log_mean_fights + (2 * log_stdev_fights)))
    }

    rarity_thresh = spirit_fighter_rarities[rarity_char]
    elligible_fighters = {fighter_id: total_wins for fighter_id, total_wins in log_total_fights_dict.items() if total_wins >= rarity_thresh}
    print(elligible_fighters)
    # Retrieve the SpiritFighter objects based on the filtered fighter IDs
    spirit_fighter = random.choice(SpiritFighter.objects.filter(id__in=elligible_fighters.keys()))
    return spirit_fighter

# Determine the name, prefix, and suffix of the fighter
def determine_fighter_name(rarity_char):
    # Names themselves will always be common, so just pick a random one
    name = random.choice(Name.objects.filter(rarity="C", type="N")).text
    # Prefixes and Suffixes are reserved for elite fighters.
    prefix = Name.objects.filter(rarity=rarity_char, type="P")
    suffix = Name.objects.filter(rarity=rarity_char, type="S")
    # If available, randomly select a prefix
    if prefix.exists() and len(prefix) > 0: 
        prefix = random.choice(prefix).text
    else:
        prefix = ""
    # If available, randomly select a suffix
    if suffix.exists() and len(suffix) > 0: 
        suffix = random.choice(suffix).text
    else: 
        suffix = ""
    
    return prefix, name, suffix

# Determine the "lifestyle" features of the fighter
def determine_lifestyle_features(rarity):
    pass