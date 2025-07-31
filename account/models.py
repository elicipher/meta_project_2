from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django_prose_editor.fields import ProseEditorField
from .managers import UserManager

# Create your models here.

class Member(AbstractBaseUser):

    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(unique=True , max_length=11 , verbose_name="شماره تلفن" , null= True , blank= True)
    email = models.EmailField(unique=True)  # ایمیل به عنوان فیلد یکتا (ضروری برای ورود)
    avatar = models.ImageField(upload_to="avatar/" , blank=True , null=True , verbose_name='تصویر پروفایل')
    role = models.CharField(max_length=100,null= True , blank= True , verbose_name="نقش" )
    created = models.DateTimeField(null= True , blank= True , auto_now_add= True , verbose_name="تاریخ عضویت")
    is_active = models.BooleanField(default=True , verbose_name='آیا کاربر فعاله ؟')
    is_admin = models.BooleanField(default=False , verbose_name='آیا کاربر ادمین است ؟')
    is_superuser = models.BooleanField(default=False , verbose_name='آیا کاربر مدیر است ؟')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name','email']

    objects = UserManager()

    def __str__(self):
        return self.full_name
    
    def has_perm(self , perm , obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property#وقتی یه متد رو با @property علامت می‌زنی، می‌تونی اون متد رو مثل یه ویژگی (attribute) صدا بزنی، نه مثل یه تابع.
    def is_staff(self):
        return self.is_admin


    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name  = "کاربر"
        verbose_name_plural = "کاربران"

    


    