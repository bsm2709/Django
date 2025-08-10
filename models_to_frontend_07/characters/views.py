from django.shortcuts import render  
from .models import Characters
from django.shortcuts import get_object_or_404

# Create your views here.
def characters(request):
    charac = Characters.objects.all()
    return render(request,"characters/characters.html", {'characters': charac})


def characterdetails(request, char_id):
    character = get_object_or_404(Characters, pk = char_id)
    return render()