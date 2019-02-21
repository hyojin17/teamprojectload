from django.shortcuts import render

# Create your views here.
def beauty(request):
    return render(request, 'beauty/beauty.html')