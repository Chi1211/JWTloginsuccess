from django.urls import path
from . import views
urlpatterns=[
    path('', views.ContactList.as_view()),
    path('<int:id>', views.ContactDetail.as_view())

]