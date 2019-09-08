from django.shortcuts import render
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework.views import APIView
from rest_framework import status
from rbac.utils import OopsResponse


class UserProfileView(APIView):
    """
    获取用户信息
    """
    def get_object(self, request):
        try:
            token = request.GET.get('token')
            token_info = jwt_decode_handler(token)
            return token_info
        except Exception as e:
            return e

    def get(self, request):
        data = self.get_object(request)
        return OopsResponse(data, status=status.HTTP_200_OK)


