from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import total_user


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('auth_total_user')
        self.assertEqual(resolve(url).func, total_user)
