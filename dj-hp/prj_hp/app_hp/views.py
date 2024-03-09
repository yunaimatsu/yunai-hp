from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Langinf
from django.utils.translation import gettext_lazy as _

# Create your views here.

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'file_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })

def home(request):
    my_traslatable_string = _("This is a translatable string.")
    return render(request, "home.html", {'my_translatable_string': my_traslatable_string})

def cont(request):
    return render(request, "contact.html")

def test(request):
    return render(request, "base.html")

def img_brand(request):
    return render(request, "templates/images/brand_image.png")

def lthome(request):
    return render(request, "lang-typo.html")

def ie(request):
    infos = Langinf.objects.filter()
    return render(request, "lang-typo/ie.html", {"infos": infos})

def txhome(request):
	return render(request, "taxonomy/tx-home.html")

def achi(request):
    return render(request, "achievements.html")

def orgs(request):
    return render(request, "organizations.html")
