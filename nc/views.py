from django.shortcuts import render
from .models import nC

# Create your views here.

def index(request):
    nc = nC.objects.all().count()
    return render(request, 'nc/index.html', {'nc':nc})