"""oops URL Configuration

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
from django.urls import path, re_path
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token
from rbac import views
from oops import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login', obtain_jwt_token),
    path('user/info', views.UserProfileView.as_view()),
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})

]
