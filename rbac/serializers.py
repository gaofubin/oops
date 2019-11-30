from .models import UserInfo
from rest_framework import serializers
from rbac import models


class UserViewSetSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = (
            "id",
            "email",
            "username",
            "real_name",
            "is_active",
            "password",
        )
