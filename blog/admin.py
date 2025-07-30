from django.contrib import admin
from .models import Post , Comment , Like , PostVisit

# Register your models here.

class LikeInline(admin.TabularInline):
    model = Like
    extra = 0
    readonly_fields = ('user_display',)  # فقط نمایش، قابل تغییر نیست

    def user_display(self, obj):
        if obj.user:
            return obj.user.full_name
        return "کاربر مهمان"
    user_display.short_description = 'نام کاربر'
 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','view_count','like_count','jpublish', 'status')
    inlines = [LikeInline ,]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('user','content','post','jpublish','confirme','reply',)
    ordering = ('confirme','-created',)
    search_fields = ('post','user',)
    readonly_fields = ('user_display','is_reply',)
    list_filter = ('created',)
    def user_display(self, obj):
        if obj.user:
            return obj.user.full_name
  
    
        
    



    

