from django.shortcuts import render
from .models import Characters

# Create your views here.
def characters(request):
    charac = Characters.objects.all()
    return render(request,"characters/characters.html", {'characters': charac})