from django.test import TestCase, Client
from main.models import Weapons


class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get("/main/")
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get("/main/")
        self.assertTemplateUsed(response, "main.html")

    def test_models_create_weapon(self):
        weapon = Weapons.objects.create(
            name="test",
            type="test",
            description="test",
            attack_rating=100,
            scaling=100,
            requirements=100,
            amount=100,
        )
        self.assertEqual(weapon.name, "test")
        self.assertEqual(weapon.type, "test")
        self.assertEqual(weapon.description, "test")
        self.assertEqual(weapon.attack_rating, 100)
        self.assertEqual(weapon.scaling, 100)
        self.assertEqual(weapon.requirements, 100)
        self.assertEqual(weapon.amount, 100)
