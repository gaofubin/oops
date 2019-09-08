from django.shortcuts import render
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework.views import APIView
from rest_framework import status
from rbac.utils import OopsResponse
from .models import UserProfile


class UserProfileView(APIView):
    """
    获取用户信息
    """
    def get_object(self, request):
        try:
            token = request.GET.get('token')
            token_info = jwt_decode_handler(token)
            user_info = UserProfile.objects.filter(username=token_info['username'])
            for user in user_info:
                data = {
                    "user_id": user.id,
                    "username": user.username,
                    "avatar": request._request._current_scheme_host + '/media/' + str(user.image)
                }
            print(data)
            return data
        except Exception as e:
            return e

    def get(self, request):
        data = self.get_object(request)
        return OopsResponse(data, status=status.HTTP_200_OK)


