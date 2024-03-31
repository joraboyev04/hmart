from main.models import *
from django.shortcuts import redirect, render
def Home(request):

    return render(request, 'index-2.html')

