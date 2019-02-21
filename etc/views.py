from django.shortcuts import render

# Create your views here.

def etc(request):
    return render(request, 'etc/etc.html')