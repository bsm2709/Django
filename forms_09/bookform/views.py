from django.shortcuts import render, redirect
from .forms import bookForm
from django.shortcuts import get_object_or_404
from . models import book

# Create your views here.
def home(request):
    books = book.objects.all()
    return render(request, 'bookform/home.html', {'books' : books})

def form(request):
    if request.method == "POST":
        form = bookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = bookForm()
    return render(request, 'bookform/form.html', {'form': form})