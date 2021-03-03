from .models import ContactsModel
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactsModel
        fields=['id', 'coutry_code', 'firstname', 'lastname', 'phone_number', 'contact_picture', 'owner']