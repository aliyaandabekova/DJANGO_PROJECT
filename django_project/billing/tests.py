from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class CardTest(TestCase):

    def setUp(self) -> None:
        self.url = reverse('card_create')
        self.user = User.objects.create_user(username='aliya',password='123456')
        # print(self.user.password)
        self.profile = Profile.objects.create(user=self.user,name='aliyaa',age=29,email='aliya@gmail.com')

    def test_card_create(self):
        self.client.login(username='aliya',password='123456')
        data = {
            'profile': self.profile,
            'code': 132,
            'cvv': 666,

        }
        self.response = self.client.post(self.url, data)
        print(self.response)