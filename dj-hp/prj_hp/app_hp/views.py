from django.http import HttpResponse
from django.shortcuts import render
from .models import Langinf

# Create your views here.
def home(request):
		return render(request, "home.html")

def ie(request):
	infos = Langinf.objects.filter()
	return render(request, "lang-typo/ie.html", {"infos": infos})
