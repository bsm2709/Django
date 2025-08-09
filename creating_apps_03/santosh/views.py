from django.shortcuts import render

def sanhome(request):
    return render(request, 'Santoshhome.html')

def sanabout(request):
    return render(request, 'Santoshabout.html')

def sancontact(request):
    return render(request, 'Santoshcontact.html')

def sanprojects(request):
    return render(request, 'Santoshprojects.html')

