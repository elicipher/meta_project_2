from django.db import models
from django.contrib.auth.models import AbstractUser
from django_prose_editor.fields import ProseEditorField


# Create your models here.

class Member(AbstractUser):
    AbstractUser.username = None  # حذف فیلد username
    email = models.EmailField(unique=True)  # ایمیل به عنوان فیلد یکتا (ضروری برای ورود)
    full_name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="avatar/" , blank=True , null=True , verbose_name='تصویر پروفایل')
    REQUIRED_FIELDS = [] 
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name  = "کاربر"
        verbose_name_plural = "کاربران"

    


    