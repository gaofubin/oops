from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework.views import APIView
from rest_framework import status
from .utils import OopsResponse
from .models import UserInfo
from .serializers import UserViewSetSerializers
from .service.init_permission import init_permission
from .service.init_menu import init_menu
from rest_framework.viewsets import ModelViewSet
from common.custom_pagination import MyPageNumberPagination


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


class UserViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserViewSetSerializers
    pagination_class = MyPageNumberPagination

