from accounts.models import CustomUser
from fighters.models import Cosmetic
from .models import *
import random
import numpy as np

### Function that generates a mini martial artist Fighter
def create_fighter(user_instance: CustomUser, **kwargs):
    fighter_data = {}
    # The user who is created will automatically sponsor the new fighter.
    fighter_data["sponsor"] = user_instance
    # Create a new fighter;
    # Determine the rarity of the fighter 
    rarity_char, rarity_num = determine_rarity()
    fighter_data["rarity"] = rarity_char
    # Select a Spirit Fighter based on this rarity
    spirit_fighter = determine_spirit_fighter()
    fighter_data["spirit_fighter"] = spirit_fighter
    # Determine the fighter's name based on the rarity
    prefix, suffix, name = determine_fighter_name(rarity_char=rarity_char)
    fighter_data["prefix"] = prefix
    fighter_data["name"] = name
    fighter_data["suffix"] = suffix
    # Determine biographical features based on the spirit fighter
    fighter_data["height"] = spirit_fighter.height
    fighter_data["weight"] = spirit_fighter.weight
    fighter_data["reach"] = spirit_fighter.reach
    fighter_data["stance"] = spirit_fighter.stance
    # Determine the fighter's Cosmetics
    selected_cosmetics = determine_cosmetics()
    for cosmetic_type, selected_cosmetic in selected_cosmetics.items():
        fighter_data[cosmetic_type] = selected_cosmetic
    # Determine the fighter's lifestyle features
    
    # Use the SpiritFighter's stats as priors for this current fighter
    fighter_data["stats"] = spirit_fighter.stats

    # Instatiate the fighter object
    #Fighter.objects.create(**fighter_data)

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
    elligible_fighters = {fighter_id: log_total_fights for fighter_id, log_total_fights in log_total_fights_dict.items() if (np.e**log_total_fights) >= rarity_thresh}
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
def determine_cosmetics(rarity_char, no_item_chance=0.5):
    # Find all cosmetic options that are available
    cosmetic_types = list(Cosmetic().cosmetic_choices.keys())
    cosmetics = {}
    # Select one cosmetic of each type
    for cosmetic_type in cosmetic_types:
        cosmetics[cosmetic_type] = select_cosmetic(cosmetic_type, rarity_char, no_item_chance)
    return cosmetics

# Helper function to determine_cosmetics, selects and returns one
# cosmetic after rolling down the available rarities
def select_cosmetic(cosmetic_type, rarity_char, no_item_chance):
    cosmetic_rarity_mapping = {1: "C", 2: "U", 3: "R", 4: "E", 5: "L"}
    current_rarity = cosmetic_rarity_mapping[rarity_char]
    selected_cosmetic = None
    # Filter through items by rarity, decreasing rarity as the user looks
    # through cosmetic items and returning the one that is eventually selected
    while selected_cosmetic is None and current_rarity > 0:
        #if np.random.random() > no_item_chance:
        cosmetic_options = Cosmetic.objects.filter(rarity=cosmetic_rarity_mapping[current_rarity], type="cosmetic_type")
        if len(cosmetic_options) > 0:
            selected_cosmetic = random.choice(list(cosmetic_options))
            return selected_cosmetic
        current_rarity -= 1

# Determine the "lifestyle" features of the fighter
def determine_lifestyle_features(rarity):
    pass