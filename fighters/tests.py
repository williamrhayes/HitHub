from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Fighter, CustomUser, Cosmetic
from .utils import determine_rarity, determine_fighter_name

class FighterModelTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser")

    def test_create_fighter_missing_fields(self):
        with self.assertRaises(ValidationError):
            Fighter.objects.create()  # This should raise a ValidationError

        # Add similar tests for other required fields

    def test_create_fighter_invalid_choices(self):
        with self.assertRaises(ValidationError):
            Fighter.objects.create(sponsor=None, rarity="X", stance="Invalid")

        # Add similar tests for other fields with choices

    def test_create_fighter_negative_values(self):
        with self.assertRaises(ValidationError):
            Fighter.objects.create(sponsor=None, rarity="C", height=-180, weight=-70, reach=-185)

        # Add similar tests for other numeric fields

    def test_create_fighter_lifestyle_features(self):
        fighter = Fighter.objects.create(sponsor=self.user, rarity="C", name="Test Fighter", is_offensive=True, is_badboy=False, is_athiest=True)

        self.assertTrue(fighter.is_offensive)
        self.assertFalse(fighter.is_badboy)
        self.assertTrue(fighter.is_athiest)

        # Add more tests for other lifestyle features

    def test_create_fighter_cosmetics(self):
        cosmetic = Cosmetic.objects.create(name="Test Cosmetic", type="BASE", rarity="C", primary_color="255_0_0_255", img="test.jpg")
        fighter = Fighter.objects.create(sponsor=self.user, rarity="C", name="Test Fighter", cosmetic_base=cosmetic)

        self.assertEqual(fighter.cosmetic_base, cosmetic)

        # Add more tests for other cosmetic fields

    def test_lifestyle_features_interactions(self):
        fighter1 = Fighter.objects.create(sponsor=self.user, rarity="C", name="Fighter 1", is_enlightened=True, is_badboy=False)
        fighter2 = Fighter.objects.create(sponsor=self.user, rarity="C", name="Fighter 2", is_enlightened=False, is_badboy=True)

        self.assertTrue(fighter1.is_enlightened)
        self.assertFalse(fighter1.is_badboy)

        self.assertFalse(fighter2.is_enlightened)
        self.assertTrue(fighter2.is_badboy)

        # Add more tests for other interactions

    def test_determine_rarity(self):
        rarities = ["C", "U", "R", "E", "L"]
        for _ in range(100):
            rarity = determine_rarity()
            self.assertIn(rarity, rarities)

        # Add more tests or edge cases if needed

    def test_determine_fighter_name(self):
        rarity_char = "C"  # Test with different rarity values
        prefix, name, suffix = determine_fighter_name(rarity_char)
        self.assertIsInstance(prefix, str)
        self.assertIsInstance(name, str)
        self.assertIsInstance(suffix, str)

        # Add more tests or edge cases if needed
