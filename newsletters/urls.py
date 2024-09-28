from django.urls import path
from .views import newsletter_singup, newsletter_unsubscribe

app_name='newsletters'

urlpatterns = [
    path('entrenamiento/', newsletter_singup, name='option'),
    path('unsubscribe/', newsletter_unsubscribe, name='unsubscribe'),
]


