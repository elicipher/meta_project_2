from django.db import models
from slugify import slugify

# Create your models here.
class Contact(models.Model):


    name = models.CharField(max_length=100 , verbose_name="نام کاربر")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیام")
    sended_time = models.DateTimeField(auto_now_add=True , verbose_name="زمان ارسال")
    replyed = models.BooleanField(default=False , verbose_name='پاسخ داده شده؟')
    reply = models.TextField(blank=True , null=True , verbose_name="پاسخ")
    send_time = models.DateTimeField(auto_now_add=True ,blank=True , null=True , verbose_name="تاریخ ارسال")
    reply_time = models.DateTimeField(auto_now_add=True ,blank=True , null=True , verbose_name="تاریخ پاسخ" )

    class Meta :
        verbose_name  = "پیام"
        verbose_name_plural = "پیام ها"
    
    def __str__(self):
        return f'پیام {self.message}'
    

class AboutUs(models.Model):

    title = models.CharField(max_length=200 , null= True ,blank= True ,verbose_name= "عنوان")
    image = models.ImageField(upload_to='about_us/', null= True ,blank= True , verbose_name= "تصویر" , help_text="پیشنهاد میشه سایز عکس 550 * 600 باشد")
    description = models.TextField(verbose_name="توضیحات", null= True ,blank= True )

    def __str__(self):
        return self.title


class Social(models.Model):
    ICON_CHOICES = [
        ('twitter' , 'twitter'),
        ('facebook' , 'facebook'),
        ('instagram' , 'instagram'),
        ('linkedin' , 'linkedin'),
        ('github' , 'github'),
        ('youtube' , 'youtube'),
        ('telegram' , 'telegram'),
        ('google-plus' , 'google plus'),
    ]
    about_us = models.ForeignKey(AboutUs , on_delete=models.CASCADE , null=True, blank=True,related_name='socials')
    user = models.ForeignKey('TeamMember', on_delete=models.CASCADE, null=True, blank=True , related_name="icons")
    icon = models.CharField(choices=ICON_CHOICES , max_length=100 , null=True,blank=True,verbose_name='نوع شبکه اجتماعی')
    link = models.URLField(null=True , blank= True , verbose_name="آدرس شبکه اجتماعی")


class Service(models.Model):
    ICON_CHOICES = [
        ('globe','کره'),
        ('pencil','مداد'),
        ('laptop','لپ تاپ'),
        ('film','فیلم'),
        ('user','کاربر'),
        ('handshake-o','دست دادن'),
        ('book','کتاب'),
        ('line-chart','چارت'),
        ('graduation-cap','کلاه فارغ التحصیل'),
        ('gears','چرخ دنده'),
        ('mobile','موبایل'),
        ('support','ساپورت'),
        ('rocket','موشک'),
    ]

    title = models.CharField(max_length=120 , verbose_name= "عنوان سرویس")
    icon = models.CharField(choices=ICON_CHOICES , default='globe' ,max_length=100, verbose_name="آیکن")
    description = models.CharField(max_length=300 , verbose_name= "توضیحات")

    def __str__(self):
        return self.title
    
class StatsSection(models.Model):
    ICON_CHOICES = [
        ('globe','کره'),
        ('users','کاربران'),
        ('thumbs-up','لایک'),
        ('trophy','جام'),
        ('edit','ویرایش'),
        ('gift','جایزه'),
        ('graduation-cap','کلاه فارغ التحصیل'),
        ('code','کد'),
        ('bolt','صاعقه'),
    ]
    title = models.CharField(max_length=120 , verbose_name="عنوان آمار")
    icon = models.CharField(choices=ICON_CHOICES , default='globe' ,max_length=100, verbose_name="آیکن")
    value = models.PositiveIntegerField(verbose_name="مقدار")

    def __str__(self):
        return self.title
     
class Category(models.Model):
    title = models.CharField(max_length=100 , verbose_name='عنوان دسته بندی')
    slug = models.CharField(max_length=100 , unique= True , verbose_name= 'آدرس دسته بندی')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.title



class Portfolio(models.Model):

    title = models.CharField(max_length=150, verbose_name='عنوان پروژه')
    slug = models.SlugField(max_length=100, unique=True,blank=True,allow_unicode=True , verbose_name='آدرس')
    category = models.ForeignKey(Category , on_delete= models.CASCADE , related_name= 'category', verbose_name='دسته‌بندی')
    employer = models.CharField(max_length=150, verbose_name='کارفرما')
    history = models.DateField(verbose_name='تاریخ انجام')
    address_project = models.CharField(max_length=200, verbose_name='آدرس پروژه')
    description=models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to = 'portfolio/', verbose_name='تصویر')

    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'نمونه‌کار'
        verbose_name_plural = 'نمونه‌کارها'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, separator='-', lowercase=False, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class TeamMember(models.Model):

    name = models.CharField(verbose_name = 'نام کاربر', max_length=100)
    role = models.CharField(verbose_name = 'نقش', max_length=100)
    bio = models.TextField(verbose_name = 'بیوگرافی')
    image = models.ImageField(upload_to = 'team_profile/',null = True , blank = True  , verbose_name='تصویر کاربر')

    class Meta:
        verbose_name = 'عضو تیم'
        verbose_name_plural = 'اعضای تیم'

    def __str__(self):
        return self.name