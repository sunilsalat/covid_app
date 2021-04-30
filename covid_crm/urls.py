from django.urls import path
from .views import home, Register,Find_food,Find_O2

app_name = 'covid_crm'

urlpatterns = [
    path('', home, name='home'),
    path('register', Register, name='register'),
    path('findfood',Find_food, name="findfood"),
    path('findoxygen', Find_O2, name='findoxygen') 
]