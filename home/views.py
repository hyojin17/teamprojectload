from django.shortcuts import render, get_object_or_404
from .models import Notice
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')

def notice(request):
    notices=Notice.objects
    notice_list = Notice.objects.all()

    npaginator = Paginator(notice_list,3)
    npage = request.GET.get('npage')
    nposts = npaginator.get_page(npage)
    return render(request, 'notice.html',{'notices':notices, 'nposts':nposts})

def ndetail(request, notice_id):
     ndetails = get_object_or_404(Notice, pk=notice_id)
     return render(request, 'ndetail.html', {'ndetails':ndetails})

