from django.db import models
import re

from django.db.models.base import Model
# crea las variables que se van a utilizar en la aplicacion y las validaciones 
# contienen los campos escenciales que se van a utilizar
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

#MODELS CREATIONS
class User(models.Model):
    name       = models.CharField(max_length=50)
    alias      = models.CharField(max_length=50)
    email      = models.CharField(max_length=50)
    password   = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    objects    = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    objects    = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=75)
    books = models.ManyToManyField(Book,related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    objects    = UserManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user_review = models.ForeignKey(User, related_name="user_review", on_delete=models.CASCADE)
    book_reviewed = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    objects    = UserManager()
