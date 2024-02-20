from django.http import HttpResponse
from django.shortcuts import render
from .models import Langinf

# Create your views here.
def home(request):
	return render(request, "home.html")

def cont(request):
    return render(request, "contact.html")

def test(request):
    return render(request, "base.html")

def img_brand(request):
    return render(request, "templates/images/brand_image.png")

def lthome(request):
    return render(request, "lang-typo/lt-home.html")

def ie(request):
	infos = Langinf.objects.filter()
	return render(request, "lang-typo/ie.html", {"infos": infos})

def txhome(request):
	return render(request, "taxonomy/tx-home.html")
