from django.shortcuts import render
from .models import *

# Create your views here.
def indexPage(request):
    return render(request,'index.html')