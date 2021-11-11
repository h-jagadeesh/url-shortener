from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import urls
import random,string
# Create your views here.

def index(request):
	return render(request,"gotolink/index.html")

def success(request):
	url = request.POST['link']
	l = string.ascii_lowercase
	n_link = ''.join(random.choice(l) for _ in range(6))
	print(url)
	print(n_link)
	new_data = urls(og_link = url,new_link=n_link)
	new_data.save()
	return render(request,"gotolink/success.html",{
		'new_link':n_link,
		'og_link':url
		})
def s_link(request,s_url):
	o_link = urls.objects.get(new_link = s_url)
	return redirect(o_link.og_link)
