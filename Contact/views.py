from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ContactsModel
from .serializer import ContactSerializer
from rest_framework import permissions
# Create your views here.
class ContactList(ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class=ContactSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return ContactsModel.objects.filter(owner=self.request.user)

class ContactDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated)
    serializer_class=ContactSerializer
    lookup_field="id"

    def get_queryset(self):
        return ContactsModel.objects.filter(owner=self.request.user)
        
