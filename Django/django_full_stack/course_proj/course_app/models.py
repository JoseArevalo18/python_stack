from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey, OneToOneField
from datetime import datetime

class CourseManager(models.Manager):
    def form_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "El nombre del curso debe tener mas de 5 caracteres!!"
        if len(postData['description']) < 15:
            errors['description'] = "La Descripcion debe tener mas de 15 caracteres!!"
        return errors

class Course(models.Model):
    name = CharField(max_length=50)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now_add=True)
    objects = CourseManager()

class Description(models.Model):
    description = TextField()
    course = OneToOneField(Course,on_delete=models.CASCADE,primary_key=True)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now_add=True)