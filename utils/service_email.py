from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

token_generator = PasswordResetTokenGenerator()

 
def send_email(subject, to, user, template_name):
    try:
        # ساخت توکن و لینک بازیابی
        uidb64 = urlsafe_base64_encode(force_bytes(user.id))
        token = token_generator.make_token(user)
        reset_link = f"http://127.0.0.1:8000/account/reset_password/{uidb64}/{token}/"

        # ساخت کانتکست برای قالب ایمیل
        context = {
            'user':user,
            "reset_link": reset_link
        }
        html_message = render_to_string(template_name, context)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        
    except Exception as e:
        print("خطا:", e)

#context: دیکشنری شامل داده‌هایی که به قالب اچ تی ام ال فرستاده می‌شن
#[to]: لیستی از آدرس‌های گیرنده (حتی اگر یک گیرنده داریم باید داخل لیست باشه)
