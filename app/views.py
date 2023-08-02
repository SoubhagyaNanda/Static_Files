from django.shortcuts import render

# Create your views here.

def image_inser(request):
    return render(request, 'image_insert.html')