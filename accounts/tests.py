from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpassword"))
        self.assertEqual(user.hitcoin, 1000.00)  # Default hitcoin value

    def test_create_superuser(self):
        admin_user = self.User.objects.create_superuser(
            username="adminuser",
            email="admin@example.com",
            password="adminpassword"
        )
        self.assertEqual(admin_user.username, "adminuser")
        self.assertEqual(admin_user.email, "admin@example.com")
        self.assertTrue(admin_user.check_password("adminpassword"))
        self.assertEqual(admin_user.hitcoin, 1000.00)  # Default hitcoin value
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_user_str_representation(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
        self.assertEqual(str(user), "testuser")

    def test_user_authentication(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
        authenticated_user = self.User.objects.authenticate(
            username="testuser",
            password="testpassword"
        )
        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user, user)
