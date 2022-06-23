from django.http import HttpResponse
from django.shortcuts import render
from .models import Trainee
def hello_world(request):
    trai = Trainee.objects.all()
    return render(request, 'index.html', {'trainee':trai})

