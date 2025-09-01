from django.shortcuts import render

def home(request):
    return render(request, 'beauty_home.html')
