from django.http import HttpResponse

# Create your views here.


def homeindex(request):
    response = HttpResponse(r' 全局首页在 pythonapp\pythonapp\views.py 中')
    return response
