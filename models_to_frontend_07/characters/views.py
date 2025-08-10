from django.shortcuts import render

# Create your views here.
def characters(request):
    return render(request,"characters/characters.html")