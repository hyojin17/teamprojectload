from django.shortcuts import render

# Create your views here.

def vlog(request):
    return render(request, 'vlog/vlog.html')