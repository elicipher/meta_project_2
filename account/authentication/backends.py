from django.contrib.auth.backends import BaseBackend
from account.models import Member


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = username  # به جای username همون email رو می‌گیریم
        try:
            user = Member.objects.get(email=email)
        except Member.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Member.objects.get(pk=user_id)
        except Member.DoesNotExist:
            return None
