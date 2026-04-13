from django.test import TestCase
from django.urls import reverse

from .models import VisitorName


class GreetingHomeViewTests(TestCase):
    def test_home_page_is_available(self):
        response = self.client.get(reverse("greetings:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Введите имя")

    def test_valid_name_is_saved_and_displayed(self):
        response = self.client.post(
            reverse("greetings:home"),
            {"name": "Мария"},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(VisitorName.objects.count(), 1)
        self.assertContains(response, "Мария")

    def test_blank_name_returns_validation_error(self):
        response = self.client.post(
            reverse("greetings:home"),
            {"name": "   "},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(VisitorName.objects.count(), 0)
        self.assertContains(response, "Введите имя, прежде чем отправлять форму.")
