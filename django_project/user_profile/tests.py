from django.test import TestCase
from django.urls import reverse

from .models import User, Profile

class RegisterTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('register')

    def test_register_ok(self):
        data = {
            'name':'aliya',
            'age':'19',
            'email':'aliya@gmail.com',
            'username':'aliya1',
            'password1':'django321',
            'password2':'django321'
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,200)
        # print(self.response)

    def test_register_bad_age(self):
        data = {
            'name':'aliya',
            'email':'aliya@gmail.com',
            'username':'aliya1',
            'password1':'django321',
            'password2':'django321'
        }
        self.response = self.client.post(self.url,data)
        self.assertFormError(self.response,field='age',errors='Обязательное поле.',form='form')

    def test_register_bad_name(self):
        data = {
            'age':'19',
            'email':'aliya@gmail.com',
            'username':'aliya1',
            'password1':'django321',
            'password2':'django321'
        }
        self.response = self.client.post(self.url,data)
        self.assertFormError(self.response,field='name',errors='Обязательное поле.',form='form')

    def test_register_bad_email(self):
        data = {
            'name':'aliya',
            'age':'19',
            'username':'aliya1',
            'password1':'django321',
            'password2':'django321'
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='email', errors='Обязательное поле.', form='form')

    def test_register_bad_username(self):
        data = {
            'name': 'aliya',
            'age': '19',
            'email': 'aliya@gmail.com',
            'password1': 'django321',
            'password2': 'django321'
        }

        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='username', errors='Обязательное поле.', form='form')

    def test_register_bad_password1(self):
        data = {
            'name':'aliya',
            'age':'19',
            'email':'aliya@gmail.com',
            'username':'aliya1',
            'password2':'django321'
        }

        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='password1', errors='Обязательное поле.', form='form')

    def test_register_bad_password2(self):
        data = {
            'name':'aliya',
            'age':'19',
            'email':'aliya@gmail.com',
            'username':'aliya1',
            'password1':'django321',
        }

        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='password2', errors='Обязательное поле.', form='form')
