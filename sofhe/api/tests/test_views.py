from turtle import title
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..views import addUserTask
from ..models import Event


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create(
            username='Pujan', email='pujan@gmail.com', password='pujanpujan')
        self.event = Event.objects.create(
            user=self.user, title='123', description='123', credit=123)
        return super().setUp()

    def test_add_user_task_POST(self):
        response = self.client.post(reverse('add_tasks', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 404)

    def test_user_task_GET(self):
        response = self.client.get(
            reverse('all_tasks', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 200)

    def test_edit_user_task_POS(self):
        response = self.client.post(
            reverse('edit_tasks', kwargs={'taskId': 10, 'pk': self.user.id}))
        self.assertEquals(response.status_code, 404)

    def test_delete_user_event(self):
        response = self.client.delete(
            reverse('delete_tasks', kwargs={'taskId': self.event.id, 'pk': self.user.id}))
        self.assertEquals(response.status_code, 200)
