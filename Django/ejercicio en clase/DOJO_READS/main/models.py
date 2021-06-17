from django.db import models
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-z0-9]+\.[a-zA-z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        #all the validation for the form
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Invalid name. Name must be at least 3 characters"
        if len(postData['alias']) < 2:
            errors['alias'] = "Invalid name. Alias must be at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email"
        if len(postData['password']) < 5:
            errors['password'] = "Password must be at least 6 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password does not match"
        return errors

class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()