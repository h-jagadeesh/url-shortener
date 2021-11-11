from django.shortcuts import render
from django.http import HttpResponse
from .models import urls
# Create your views here.

def index(request):
	return render(request,"gotolink/index.html")

def success(request):
	#url = 
	return render(request,"gotolink/success.html")