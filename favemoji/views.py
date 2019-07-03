import time
from django.views import generic
from django.shortcuts import render
from .models import EmojiInfo


# Create your views here.

# class IndexView(generic.ListView):
# 哪个通用视图合适呢？我想不好，还是继续用自己的自定义函数


def index(request):
    # 只有一个字符串的首页，第一版 is out
    # response=HttpResponse('FavEmoji 的首页')
    # return response
    allemojis = EmojiInfo.objects.all()
    ctime = time.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}%S{s}").format(y='年', m='月', d='日', h="时", m1="分", s="秒")
    context = {'emojilist': allemojis, 'current_time': ctime}
    return render(request, 'favemoji/2col.html', context)


class EmojiInfoDetailView(generic.ListView):
    template_name = "favemoji/detail_EmojiInfo.html"
    context_object_name = 'all_list'

    def get_queryset(self):
        return EmojiInfo.objects.all()
    
