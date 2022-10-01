
from django.test import TestCase
from ..models import Event
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='Pujan', email='pujan@gmail.com', password='pujanpujan')

    def test_add_record_event(self):
        new_record = Event.objects.create(
            user=self.user, title='hello', credit=11.9999)
        self.assertEqual(new_record.user.username, 'Pujan')
        self.assertEqual(new_record.title, 'hello')
        self.assertEqual(new_record.credit, 11.9999)
