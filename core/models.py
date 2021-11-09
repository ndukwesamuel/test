from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     firsname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     email =  models.EmailField(max_length=254,unique=True)


class blog(models.Model):
    # user = models.OneToOneField('User',on_delete=models.CASCADE, related_name="user")
    title= models.CharField(max_length=200)
    body = models.TextField()


    def __str__(self):
        return self.title
