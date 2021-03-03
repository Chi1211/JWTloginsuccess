from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ContactsModel(models.Model):
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE)
    coutry_code=models.CharField(max_length=255)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=15)
    contact_picture=models.URLField(null=True)

    def __str__(self):
        return self.firstname