from django.urls import path

from . import views

# Це для того що б Django точно знав що ці urls відносяться до певної аппки 
app_name = "polls"

urlpatterns = [
    # Для загрузки основної сторінки 
    path("", views.index, name="index"),
    # Це обробка форми описана в views.py 
    path('send-contact/', views.contact_view, name='send_contact'),
]
