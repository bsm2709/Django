from django.shortcuts import render

# Create your views here.
def C_home(request):
    return render(request, 'cards/C_home.html')

def about(request):
    return render(request, 'cards/about.html')