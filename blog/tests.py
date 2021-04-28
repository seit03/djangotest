from pyexpat import model

from django.forms import ModelForm
from django.test import TestCase

# Create your tests here.
from blog.forms import PostForm
from blog.models import Post


class TestForms(TestCase):

    def test_post_form(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }
        post = Post.objects.create(**post_info)
        form = PostForm(post_info)
        self.assertEqual(post.title, post_info['title'])
        self.assertEqual(post.description, post_info['description'])
        self.assertEqual(post.image, post_info['image'])


class TestModels(TestCase):
    def test_post_creation(self):
        test_post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }

    def test_post_update(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }

    def test_post_delete(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }

    def test_post_creation_fail(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }

    def test_comment_creation(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }

    def test_comment_update(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }

    def test_comment_delete(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }

    def test_comment_creation_fail(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }
    post = Post.objects.create(**test_post_creation)
    form = ModelForm(test_post_update)
    self.assertEqual(model.title, test_post_delete['title'])
    self.assertEqual(model.description, test_post_creation_fail['description'])
    self.assertEqual(model.image, test_comment_creation['image'])


class Test_Views(TestCase):
    def test_get_post(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }
        pass

    def test_get_comment(self):
        post_info = {
            'title': 'test title',
            'description': 'description',
            'image': 'media/posts/315302_tsA2Csf.jpg'
        }
        pass
