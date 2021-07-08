from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    def __repr__(self):
        return f"<Usuario object: {self.first_name} {self.last_name} {self.email_address} {self.age} ({self.id})"
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()