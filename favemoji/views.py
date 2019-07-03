import time
from django.views import generic
from django.shortcuts import render
from .models import EmojiInfo, FavEmoji


# Create your views here.

# class IndexView(generic.ListView):
# 哪个通用视图合适呢？我想不好，还是继续用自己的自定义函数


def index(request):
    # 只有一个字符串的首页，第一版 is out
    # response=HttpResponse('FavEmoji 的首页')
    # return response
    allemojis = EmojiInfo.objects.all()
    allfavemojis = FavEmoji.objects.all()
    ctime = time.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}%S{s}").format(
        y='年', m='月', d='日', h="时", m1="分", s="秒")

    context = {'allemojis': allemojis,
               'current_time': ctime, 'allfavemojis': allfavemojis, }
    return render(request, 'favemoji/2col.html', context)


def hello(request):
    return render(request, 'hello.html')


class EmojiInfoDetailView(generic.ListView):
    template_name = "favemoji/detail_EmojiInfo.html"
    allemojis = EmojiInfo.objects.all()
    allfavemojis = FavEmoji.objects.all()
    ctime = time.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}%S{s}").format(
        y='年', m='月', d='日', h="时", m1="分", s="秒")
    context_object_name = {'all_list': allemojis,
                           'current_time': ctime, 'allfavemojis': allfavemojis}

    def get_queryset(self):
        return EmojiInfo.objects.all()
