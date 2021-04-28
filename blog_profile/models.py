from django.db import models

MALE = 1
FEMALE = 2
GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)


class Profile(models.Model):
    name = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER,
                                 verbose_name='gender')
    bio = models.TextField()
    image = models.ImageField(upload_to='profile/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.login}'
