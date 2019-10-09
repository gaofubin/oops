from django.shortcuts import render
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework.views import APIView
from rest_framework import status
from rbac.utils import OopsResponse
from .models import UserInfo, Role, Menu
from .service.init_permission import init_permission
from .service.init_menu import init_menu
from django.conf import settings


class UserInfoView(APIView):
    """
    获取用户信息
    """

    def get(self, request):
        token = request.GET.get('token')
        token_info = jwt_decode_handler(token)
        user_obj = UserInfo.objects.filter(username=token_info['username']).first()
        init_permission(request, user_obj)
        menus = init_menu(request)
        data = {
            "user_id": user_obj.id,
            "username": user_obj.username,
            "avatar": request._request._current_scheme_host + '/media/' + str(user_obj.image),
            "menus": menus
        }
        return OopsResponse(data, status=status.HTTP_200_OK)



