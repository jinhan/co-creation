from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

import os
import sys

import cgi_exe
from platformAdapter import OSHelper

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.
class Settings:
    settings = []
    def __init__(self):
        self.settings = self.settings

    def resetSettings(self):
        self.settings = []

    def addSettings(self, v):
        self.settings.append(v)

    def deleteSettings(self):
        self.settings = self.settings[:-1]

    def getSettings(self):
        return self.settings

settings = Settings()

def intro(request):
    settings.resetSettings()
    response = render(request, 'app/intro.html', {})
    return response

@csrf_exempt
def selection1(request):
    if request.method == "POST":
        pk = request.POST.get('pk', None)
        print(pk)
        settings.addSettings(pk)

    html = render_to_string('app/selection1.html', {})
    return HttpResponse(html)

@csrf_exempt
def selection2(request):
    if request.method == "POST":
        pk = request.POST.get('pk', None)
        print(pk)
        settings.addSettings(pk)

    html = render_to_string('app/selection2.html', {})
    return HttpResponse(html)

@csrf_exempt
def selection3(request):
    if request.method == "POST":
        pk = request.POST.get('pk', None)
        print(pk)
        settings.addSettings(pk)

    html = render_to_string('app/selection3.html', {})
    return HttpResponse(html)

@csrf_exempt
def mode(request):
    if request.method == "POST":
        pk = request.POST.get('pk', None)
        print(pk)
        settings.addSettings(pk)
    mode = settings.getSettings()
    if mode[0] == 'draw':
        html = render_to_string('app/draw.html', {'settings': mode})
    elif mode[0] == 'help':
        html = render_to_string('app/help_noAI.html', {'settings': mode})
    return HttpResponse(html)

@csrf_exempt
def goBack(request):
    settings.deleteSettings()
    url = "{0}/{1}".format(request.META.get('HTTP_REFERER', '/'), "http://localhost:8000")
    return HttpResponseRedirect(url)

class ImgBlobData:
    def __init__(self):
        self.img_blob_src = ""

    def writeData(self, src):
        self.img_blob_src = src

    def readData(self):
        return self.img_blob_src

img_blob_src = ImgBlobData()

@csrf_exempt
def colorize(request):
    if "id" in request.POST.keys():
        id_str = request.POST.get("id", None)
        print(id_str)

    if "img_src" in request.POST.keys():
        img_uri = request.POST.get("img_src", None)
        img_blob_src.writeData(img_uri)

    html = render_to_string('app/colorize.html', {"img_src": img_blob_src.readData()})
    return HttpResponse(html)


@csrf_exempt
def colorize_post(request):
    if "id" in request.POST.keys():
        id_str = request.POST.get("id", None)
        print(id_str)

    module_dir = os.path.dirname(__file__)
    if "line" in request.FILES.keys():
        bin1 = request.FILES.getlist("line")[0]
        print(bin1)
        fout1 = os.path.join(module_dir + '/static/paintschainer'+ '/images/line/'+ id_str + ".png")
        path = default_storage.save(fout1, ContentFile(bin1.read()))
        print(fout1)

    if "ref" in request.FILES.keys():
        bin2 = request.FILES.getlist("ref")[0]
        print(bin2)
        fout2 = os.path.join(module_dir + '/static/paintschainer'+'/images/ref/'+id_str +".png")
        path2 = default_storage.save(fout2, ContentFile(bin2.read()))

    html = render_to_string('app/colorize.html', {})
    return HttpResponse(html)

@csrf_exempt
def colorize_paint(request):
    if "id" in request.POST.keys():
        id_str = request.POST.get("id", None)
        print("id_str:"+id_str)

    blur = 0
    if "blur" in request.POST.keys():
        blur = request.POST.get("blur", None)
        try:
            blur = int(blur)
        except ValueError:
            blur = 0
        print("blur:" + blur)

    painter = cgi_exe.Painter(gpu=0)
    # painter.colorize(id_str, request.POST.get("step", None) if "step" in request.POST.keys() else "C", blur=blur)
    painter.colorize(id_str, 'C', blur=blur)

    html = render_to_string('app/colorize.html', {})
    return HttpResponse(html)
