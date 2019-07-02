from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeproc(request):
    response=HttpResponse(' 这里是首页，等待完善')
    
    return response
    

def favemoji(request):
    """ 
    显示一个页面，分左右区。左边是已经选定的Emoji区。右边是所有的Emoji区。
    左区再分上下。上区，显示，下区用于编辑。以及输出。
    
    """
    
    response=HttpResponse('进入APP')
    return response