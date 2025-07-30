from django.db import models
from django.utils import timezone 
from account.models import Member
from django_prose_editor.fields import ProseEditorField
from slugify import slugify
from utils.date_utils import time_Converter


# Create your models here.
class Post(models.Model):
    
    STATUS_CHOICES =(
        ('d' , 'پیش نویس'),
        ('p' , 'منتشر شده'),
    )
    
    title = models.CharField(max_length=100 , verbose_name='عنوان پست')
    slug = models.SlugField(max_length=100 ,unique=True,blank=True, allow_unicode=True, verbose_name='آدرس')
    image = models.ImageField(upload_to='Post_Images/' , blank=True , null=True , verbose_name="تصویر پست")
    description = ProseEditorField(verbose_name='محتوای مقاله')
    publish = models.DateTimeField(default=timezone.now , verbose_name="زمان انتشار" )
    created = models.DateField(auto_now_add=True , verbose_name='تاریخ ساخت')
    updated = models.DateField(auto_now=True , verbose_name='تاریخ بروز رسانی')
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES , verbose_name= "وضعیت")
    author = models.ForeignKey(Member ,on_delete=models.CASCADE, related_name='post_author',verbose_name='نویسنده')
    
    class Meta():
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        
    def like_count(self):
        return self.post_like.count()
    
    def view_count(self):
        return self.views.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, separator='-', lowercase=False, allow_unicode=True)
        super().save(*args, **kwargs)

    def jpublish(self):
        return time_Converter(self.publish)
    jpublish.short_description = 'زمان انتشار'
    view_count.short_description = 'تعداد بازدید'
    like_count.short_description = 'تعداد لایک'



    
    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post , on_delete= models.CASCADE , related_name='post_like' ) 
    user = models.ForeignKey(Member , on_delete= models.CASCADE , blank= True , null= True , related_name='liked_post' , verbose_name='کاربر') 
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = " لایک ها"
    
    
    def __str__(self):
        return f"{self.user} لایک {self.post.title}"
    
class PostVisit(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='views')
    ip_address = models.GenericIPAddressField(null=True , blank= True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'بازدید از {self.post.title} از آدرس {self.ip_address}'
    




    
class Comment(models.Model):

    post = models.ForeignKey(Post , on_delete= models.CASCADE , related_name="postcomment" , verbose_name='پست')
    user = models.ForeignKey(Member , on_delete=models.CASCADE , related_name='usercomment' , verbose_name='کاربر')
    content = models.TextField(max_length=500,verbose_name="متن کامنت")
    confirme = models.BooleanField(default=False , verbose_name='تایید شده')
    created = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ ارسال')
    reply = models.ForeignKey('self',on_delete=models.CASCADE , related_name='replies', verbose_name='پاسخ', null=True , blank=True )
    is_reply = models.BooleanField(default=False)

    class Meta():
        verbose_name = "نظر"
        verbose_name_plural = "نظرات" 
    def __str__(self):
        return f'کامنت {self.user} : "{self.content}'
    
   
    
    def jpublish(self):
        return time_Converter(self.created)
    
    jpublish.short_description = "تاریخ انتشار"
