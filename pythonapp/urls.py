"""pythonapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views as topviews


urlpatterns = [
    # path('', topviews.homeproc, name='topindex'),
    # 默认app 也可以产生views , 只不过模式要求只想到另外的工作APP
    path('', topviews.homeindex, name='index'),
    path('favemoji/', include('favemoji.urls')),
    path('admin/', admin.site.urls),
]
