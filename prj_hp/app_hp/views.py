from django.shortcuts import render

# Create your views here.
def home(request):
		return render(request, "home.html")

def ie(request):
		return render(request, "lang-typo/ie.html")

