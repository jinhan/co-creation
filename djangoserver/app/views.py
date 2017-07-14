from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


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
def draw(request):
    if request.method == "POST":
        pk = request.POST.get('pk', None)
        print(pk)
        settings.addSettings(pk)

    html = render_to_string('app/draw.html', {'settings': settings.getSettings()})
    return HttpResponse(html)

@csrf_exempt
def goBack(request):
    settings.deleteSettings()
    url = "{0}/{1}".format(request.META.get('HTTP_REFERER', '/'), "http://localhost:8000")
    return HttpResponseRedirect(url)
