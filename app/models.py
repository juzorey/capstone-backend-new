from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from django.contrib.auth import get_user_model

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    body = models.TextField()


class User(models.Model):
    user = get_user_model()
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user


class MyUserManager(BaseUserManager):

    def create_user(self, username, email, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=self.normalize_user(username),
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user



    # name = models.CharField(max_length=255)
    # email = models.CharField(max_length=255, unique=True)
    # password = models.CharField(max_length=255)
    # username = None
    # weight = None
    # USERNAME_FIELD = 'email'
    # # we want to log in with an email and a password and not the django default of username and password (see if we can change this!)
    # REQUIRED_FIELDS = []

    # def __str__(self):
    #     return self.name
    


# In order to keep your code generic, use the get_user_model() method to retrieve the user model and the AUTH_USER_MODEL setting to refer to it when defining model's relations to the user model, instead of referring to the auth user model directly.

# https://stackoverflow.com/questions/12921789/django-import-auth-user-to-the-model
# https://stackoverflow.com/questions/50805337/how-do-you-serialize-the-user-model-in-django-rest-framework