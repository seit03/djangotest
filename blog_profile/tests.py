from django.test import TestCase, Client
from blog_profile.models import Profile

class TestModels(TestCase):

    def test_create_profile_success(self):
        profile_info = {
            'name': 'TestName',
            'login': 'TestLogin',
            'age': 24,
            'gender': 1,
            'bio': 'testbio',
            'image': 'media/posts/315302.jpg'
        }
        profile = Profile.objects.create(**profile_info)
        self.assertEqual(profile.name, profile_info['name'])
        self.assertEqual(profile.login, profile_info['login'])
        self.assertEqual(profile.age, profile_info['age'])
        self.assertEqual(profile.gender, profile_info['gender'])
        self.assertEqual(profile.bio, profile_info['bio'])
        self.assertEqual(profile.image, profile_info['image'])

    def test_profile_creation_fail(self):
        profile_info = {
            'name': 'SmartName',
            'login': 'SmartLogin',
            'age': 'smartage',
            'gender': 'male',
            'bio': 'bio',
            'image': 'media/posts/315302.jpg'
        }
        with self.assertRaises(ValueError):
            profile = Profile.objects.create(**profile_info)

    def test_update_profile(self):
        profile_info = {
            'name': 'Adilet',
            'login': 'Adi',
            'age': 24,
            'gender': 1,
            'bio': 'bio',
            'image': 'media/posts/315302.jpg'
        }
        new_login = 'TELIDAS'
        profile = Profile.objects.create(**profile_info)
        profile.login = new_login
        profile.save()
        profile.refresh_from_db()
        self.assertEqual(profile.login, new_login)

    def test_delete_profile(self):
        profile_info = {
            'name': 'SmartName',
            'login': 'SmartLogin',
            'age': 24,
            'gender': 1,
            'bio': 'bio',
            'image': 'media/posts/315302.jpg'
        }
        profile = Profile.objects.create(**profile_info)
        pk = profile.pk
        profile.delete()
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(pk=pk)


class TestViews(TestCase):

    def test_get_detail(self):
        profile_info = {
            'name': 'TestName',
            'login': 'TestLogin',
            'age': 24,
            'gender': 1,
            'bio': 'testbio',
            'image': 'media/posts/315302.jpg'
        }
        profile = Profile.objects.create(**profile_info)
        client = Client()
        response = client.get(path=f'/profiles/{profile.pk}/')
        self.assertEqual(response.status_code, 200)
