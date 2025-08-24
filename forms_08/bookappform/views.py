from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'bookappform/home.html')

def form(request):
    return render(request, 'bookappform/forms.html')