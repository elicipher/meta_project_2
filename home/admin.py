from django.contrib import admin
from .models import Contact , Service , StatsSection , Category , Portfolio , TeamMember
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
# Register your models here.


admin.site.register(StatsSection)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(TeamMember)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','replyed','sended_time',)
    ordering = ('-sended_time','replyed',)
    list_filter = ('replyed','sended_time')
    readonly_fields = ('name','email','message','replyed')

    def save_model(self, request, obj, form, change):
        if 'reply' in form.changed_data and obj.reply: #بررسی اینکه فیلد پاسخ تغییر کرده و خالی نباشه
            self.send_mail_to_user(obj)
            obj.replyed = True
        super().save_model(request, obj, form, change)

    def send_mail_to_user(request , contact):
        #contact همون obj  ایه که تو خط پانزده ارسال کردیم
        context = {
            'user_message': contact.message,
            'admin_response': contact.reply,

        }
        subject = 'پاسخ به پیام شما'
        from_email = settings.EMAIL_HOST_USER
        to_email = contact.email
        html_message = render_to_string('home/reply_email.html',context)
        plain_message = strip_tags(html_message)

        send_mail(subject ,plain_message, from_email , [to_email] ,html_message=html_message)
