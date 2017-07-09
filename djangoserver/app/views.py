from django.shortcuts import render

# Create your views here.
def draw(request):
    response = render(request, 'app/index.html', {})
    return response
