from django.shortcuts import render



def home(request):
    return render(request, 'home.html')

def notice(request):
    return render(request, 'notice.html')
