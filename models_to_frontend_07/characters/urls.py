
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.characters, name = 'characters'),
    path('<int:char_id>/', views.characterdetails , name = 'char_details')

]
