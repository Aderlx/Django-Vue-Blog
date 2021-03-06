"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from core import views
from Blog import settings
from django.views.static import serve


# api
router_api = routers.DefaultRouter()
router_api.register(r'profile', views.ProfileViewSet)
router_api.register(r'tag', views.TagViewSet)
router_api.register(r'category', views.CategoryViewSet)
router_api.register(r'article', views.ArticleViewSet)

# user


urlpatterns = [
    # 接口
    path('api/', include(router_api.urls)),

    # 登录
    path('auth/login/', obtain_jwt_token),

    # 权限认证
    path('auth/user/', views.UserViewSet.as_view({
        "get": "auth"
    })),

    # 媒体文件
    re_path('^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),

]
