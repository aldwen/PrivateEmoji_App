from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeproc(request):
    response=HttpResponse(' 这里是首页，等待完善')
    
    return response
    
def favemoji(request):
    response=HttpResponse('进入APP')
    return response