from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeproc(request):
    response=HttpResponse(r' 全局首页在 pythonapp\pythonapp\views.py 中')
    
    return response
    
