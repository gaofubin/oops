from .models import UserProfile
from rest_framework import serializers


# class UserProfileSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = (
#             "id",
#             "username",
#         )