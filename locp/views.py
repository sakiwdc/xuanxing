from django.http import HttpResponse
from django.shortcuts import render

from .models import Leixin, HunhePeizhi, DuliPeizhi

def index(request):
    return HttpResponse("欢迎进入服务器选配系统")
    return render(request, 'index.html', context={'类型':Leixin})
# Create your views here.
