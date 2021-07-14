from __future__ import unicode_literals
from django.db import models
from datetime import date

class ShowManager(models.Manager):
    def form_validator(self, postData):
        errors = {}
        print(postData['is_edit'])
        current_date = date.today()
        if len(postData['titleInput']) < 2:
            errors['titleInput'] = "El Titulo debe tener al menos 2 caracteres"
        if Show.objects.filter(title=postData['titleInput']).exists():
            if postData['is_edit'] == 'no':
                errors['titleInput'] = "El Show Ya Existe!!"
        if len(postData['networkInput']) < 3:
            errors['networkInput'] = "La Televisora debe tener al menos 3 caracteres"
        if len(postData['descriptionInput']) != 0:
            if len(postData['descriptionInput']) < 10:
                errors['descriptionInput'] = "La Descripcion debe tener al menos 10 caracteres"
        if postData['dateInput'] > current_date.strftime("%Y-%m-%d"):
            errors['dateInput'] = "La fecha del show no puede estar hoy o en el futuro"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
