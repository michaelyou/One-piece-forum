# coding: utf-8

from django.contrib.auth.backends import ModelBackend # 继承这个为了使用admin的权限控制
from forum.models import ForumUser

#验证用户登录，注册到setting中的AUTHENTICATION_BACKENDS
class UserAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = ForumUser.objects.get(username=username)
            if user.check_password(password):
                return user
            return None
        except ForumUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return ForumUser.objects.get(pk=user_id)
        except ForumUser.DoesNotExist:
            return None