from django.db import models

# Create your models here.
class Contact(models.Model):


    name = models.CharField(max_length=100 , verbose_name="نام کاربر")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیام")
    sended_time = models.DateTimeField(auto_now_add=True , verbose_name="زمان ارسال")
    replyed = models.BooleanField(default=False , verbose_name='پاسخ داده شده؟')
    reply = models.TextField(blank=True , null=True , verbose_name="پاسخ")

    class Meta :
        verbose_name  = "پیام"
        verbose_name_plural = "پیام ها"
    
    def __str__(self):
        return f'پیام {self.message}'
