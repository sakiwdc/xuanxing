from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎进入服务器选配系统")
# Create your views here.
