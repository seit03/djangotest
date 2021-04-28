from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', null=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)