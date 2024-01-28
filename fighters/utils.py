from accounts.models import CustomUser
from fighters.models import Cosmetic
from .models import *
import random
import numpy as np

### Function that generates a mini martial artist Fighter
def create_fighter(user_instance: CustomUser=None, rarity=None, **kwargs):
    fighter_data = {}
    # The user who is created will automatically sponsor the new fighter.
    fighter_data["sponsor"] = user_instance
    # Create a new fighter;
    # Determine the rarity of the fighter randomly unless
    # explicitly set
    rarity_char = determine_rarity()
    if rarity: rarity_char = rarity
    fighter_data["rarity"] = rarity_char
    # Select a Spirit Fighter based on this rarity
    spirit_fighter = determine_spirit_fighter(rarity_char=rarity_char)
    fighter_data["spirit_fighter"] = spirit_fighter
    # Determine the fighter's name based on the rarity
    prefix, name, suffix = determine_fighter_name(rarity_char=rarity_char)
    fighter_data["prefix"] = prefix
    fighter_data["name"] = name
    fighter_data["suffix"] = suffix
    # Determine biographical features based on the spirit fighter
    fighter_data["height"] = spirit_fighter.height
    fighter_data["weight"] = spirit_fighter.weight
    # Use stats from the ratio of reach to height to randomly assign a reach
    fighter_data["reach"] = spirit_fighter.height * np.random.normal(loc=1.0241625667652927, scale=0.0280589219520499)
    fighter_data["stance"] = spirit_fighter.stance
    # Determine the fighter's Cosmetics
    selected_cosmetics = determine_cosmetics(rarity_char=rarity_char)
    for cosmetic_type, selected_cosmetic in selected_cosmetics.items():
        fighter_data[cosmetic_type] = selected_cosmetic
    # Determine the fighter's lifestyle features
    lifestyle_features = determine_lifestyle_features(rarity_char=rarity_char)
    for lifestyle_feature, is_active in lifestyle_features.items():
        fighter_data[lifestyle_feature] = is_active
    # Use the SpiritFighter's stats as priors for this current fighter
    fighter_data["priors"] = spirit_fighter.stats
    
    # Instatiate the fighter object
    Fighter.objects.create(**fighter_data)

# Determine the rarity of the fighter
def determine_rarity():
    rank_rarities = {"C": 1, "U": 1/4, "R": 1/32, "E": 1/256, "L": 1/2048}
    rando = np.random.random()
    if rando <= rank_rarities["L"]: return "L"
    if rando <= rank_rarities["E"]: return "E"
    if rando <= rank_rarities["R"]: return "R"
    if rando <= rank_rarities["U"]: return "U"
    return "C"

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
    sample_cosmetic = Cosmetic()
    cosmetic_types = list(sample_cosmetic.cosmetic_choices.keys())
    cosmetics = {}
    # Select one cosmetic of each type
    for cosmetic_type in cosmetic_types:
        cosmetic_reference = f"cosmetic_{cosmetic_type.lower()}"
        cosmetics[cosmetic_reference] = select_cosmetic(cosmetic_type, rarity_char, no_item_chance)
    return cosmetics

# Helper function to determine_cosmetics, selects and returns one
# cosmetic after rolling down the available rarities
def select_cosmetic(cosmetic_type, rarity_char, no_item_chance):
    rarity_char_to_num = {'C': 1, 'U': 2, 'R': 3, 'E': 4, 'L': 5}
    rarity_num_to_char = {1: 'C', 2: 'U', 3: 'R', 4: 'E', 5: 'L'}
    current_rarity = rarity_char_to_num[rarity_char]
    selected_cosmetic = None
    # Filter through items by rarity, decreasing rarity as the user looks
    # through cosmetic items and returning the one that is eventually selected
    while selected_cosmetic is None and current_rarity > 0:
        #if np.random.random() > no_item_chance:
        cosmetic_options = Cosmetic.objects.filter(rarity=rarity_num_to_char[current_rarity], type="cosmetic_type")
        if len(cosmetic_options) > 0:
            selected_cosmetic = random.choice(list(cosmetic_options))
            return selected_cosmetic
        current_rarity -= 1

# Determine the "lifestyle" features of the fighter
def determine_lifestyle_features(rarity_char, offensive_roll=0.2, badboy_roll=0.1, athiest_roll=0.05, enlightenment_roll=0.05, derranged_roll=0.05, radioactive_roll=0.03, abstinence_roll=0.01):
    # Correlated features are
    # Abstinence and enlightenment
    # Athiest is more likely to make the fighter a badboy
    # Offensive, and badboy/derranged are correlated
    # If they are enlightened they can't be badboy
    # If they are derranged they can't be enlightened or badboy
    rarity_mapping = {'C': 1, 'U': 2, 'R': 3, 'E': 4, 'L': 5}
    current_rarity = rarity_mapping[rarity_char]
    is_offensive = random.random() <= offensive_roll # Sometimes fighters are just offensive
    is_badboy = False
    is_enlightened = False
    is_derranged = False
    is_radioactive = False
    is_athiest = False
    is_abstinent = False
    is_badboy = False

    # Each rarity rank gives the fighter a roll to be either 
    # enlightened or athiest
    while current_rarity > 0:
        is_badboy = random.random() <= badboy_roll
        is_enlightened = random.random() <= enlightenment_roll
        is_athiest = random.random() <= athiest_roll
        is_derranged = random.random() <= derranged_roll
        is_radioactive = random.random() <= radioactive_roll
        current_rarity -= 1
    
    # Athiesm has a bonus chance of enlightenment, abstinence, and being a badboy
    if is_athiest:
        is_enlightened = random.random() <= enlightenment_roll * 2
        is_badboy = random.random() <= badboy_roll * 5
        is_abstinent = random.random() <= abstinence_roll * 10

    # Enlightenment is mutually exclusive with being a badboy
    if is_enlightened:
        is_badboy = False
        is_offensive = False
        is_abstinent = True

    # If you're derranged you can't be enlightened or badboy, you're just nuts.
    # Also have a higher chance of being radioactive
    if is_derranged:
        is_enlightened = False
        is_badboy = False
        is_offensive = random.random() <= offensive_roll * 1.5
        is_radioactive = random.random() <= radioactive_roll * 1.5

    # Badboys are 5x more likely to be offensive
    if is_badboy:
        is_offensive = random.random() <= radioactive_roll * 5
    
    lifestyle_features = {
        "is_offensive": is_offensive,
        "is_badboy": is_badboy,
        "is_enlightened": is_enlightened,
        "is_derranged": is_derranged,
        "is_radioactive": is_radioactive,
        "is_athiest": is_athiest,
        "is_abstinent": is_abstinent,
        "is_badboy": is_badboy,
    }

    return lifestyle_features