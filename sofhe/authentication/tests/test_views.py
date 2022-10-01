from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.list_url = reverse('auth_total_user')
        self.user = User.objects.create(
            username='Pujan', email='pujan@gmail.com', password='pujanpujan')
        return super().setUp()

    def test_user_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.last().email, 'pujan@gmail.com')
