from django.shortcuts import render, get_object_or_404, redirect
from .models import Recommand
from django.utils import timezone




def recommand(request):
    recommands = Recommand.objects
    return render(request, 'recommand.html', {'recommands': recommands})

def detail(request, recommand_id):
    details = get_object_or_404(Recommand, pk=recommand_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터베이스에 넣어주는 함수
    recommand = Recommand()#Blog라는 클래스로부터 blog라는 객체를 하나 생성
    recommand.title = request.GET['title']#블로그 객체안에 title을 넣어준다.
    recommand.body = request.GET['body']
    recommand.pub_date = timezone.datetime.now()#이것을 쓰기 위해 위에 import해준다.
    recommand.save()#지금까지 객체에 넣은 내용을 데이터베이스에 저장해라
    return redirect('/recommand/'+str(recommand.id))




