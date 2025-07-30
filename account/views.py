from django.shortcuts import render , redirect
from django.views import View
from .models import Member
from django.contrib import messages
from django.contrib.auth import login , logout
from .forms import UserRegitrationForm , UserLoginForm ,EditProfileForm , ForgotPasswordForm,ResetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from utils.service_email import send_email
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


token_generator = PasswordResetTokenGenerator()
# Create your views here.

class RegisterView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    template_name = 'account/user_register.html'
    form_class = UserRegitrationForm

    def get(self , request):
        form = self.form_class()
        return render(request , self.template_name , {'form':form})
        

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            full_name = cd.get('full_name')
            email = cd.get('email')
            password = cd.get('password')
            new_member = Member(full_name=full_name , email = email )
            new_member.set_password(password)
            new_member.save()
            login(self.request,new_member)
            messages.success(request , "ثبت نام با موفقیت انجام شد" , "success")
            return redirect('home:home')
        return render(request ,self.template_name , {"form" : form})

class LoginView(View):
    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next', '/')
        return super().setup(request, *args, **kwargs)
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    template_name = 'account/user_login.html'
    form_class = UserLoginForm

    def get(self , request):
        form = self.form_class()
        return render(request , self.template_name , {"form": form})

    def post(self , request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.user
            login(request , user)
            request.session['reset_email'] = user.email
            messages.success(request ,"شما با موفقیت وارد حساب کاربریتان شدید  " , "success")
            if self.next:
                return redirect(self.next)
            return redirect('home:home')
        else:
        # اگر لاگین ناموفق بود، ایمیل وارد شده را ذخیره کن
            email = request.POST.get('email', '') 
            request.session['reset_email'] = email
            return render(request, self.template_name, {'form': form})
        
        

class LogoutView(LoginRequiredMixin , View):
        def get(self,request):
            logout(self.request)
            messages.success(request , "شما با موفقیت از حساب کاربریتان خارج شدید" , "success")
            return redirect('home:home')


class EditProfileView(LoginRequiredMixin,View):
    form_class = EditProfileForm
    template_name = 'account/user_profile.html'
    
    def get(self , request):
        form = self.form_class(instance=request.user , initial={"full_name":request.user.full_name ,'email':request.user.email , "avatar":request.user.avatar})
        return render(request , self.template_name , {'form': form})

    def post(self, request):
        form = self.form_class(request.POST , request.FILES , instance = request.user)
        if form.is_valid():
            form.save()
            request.user.full_name = form.cleaned_data['full_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request , "پروفایل شما با موفقیت عوض شد" , 'success')
        return redirect("account:user_profile")

class ForgetPasswordView(View):
    form_class = ForgotPasswordForm
    template_name = 'account/forget_password.html'

    def get(self , request):
        email = request.session.get('reset_email', '')
        form =self.form_class(initial={'email':email})
        return render(request , self.template_name , {'form':form})


    def post(self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = Member.objects.filter(email__iexact=email).first()
            #iexact جست و جو بدون حساسیت کوچیک و بزرگی حروف
            #first() اولین کاربری که با این ایمیل یافت شد
            send_email("بازیابی رمز عبور",user.email , user, 'account/email_template.html')
            messages.success(request,'درخواست شما ارسال شد . لطفا ایمیل تان را چک کنید ')

        return render(request , self.template_name , {'form':form})
        
class ResetPasswordView(View):
    form_class = ResetPasswordForm
    template_name = 'account/reset_password.html'

    def get(self , request ,uidb64 , token):
        form = self.form_class()
        return render(request , self.template_name , {"form":form})
    
    def post(self , request ,uidb64 , token):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                uid = urlsafe_base64_decode(uidb64).decode()
                #اینجا از تابع urlsafe_base64_decode استفاده می‌کنیم تا مقدار اصلی شناسه را به دست آوریم.
                #decode()= تبدیل میکنه به رشته متنی
                user = Member.objects.get(id = uid)
                if token_generator.check_token(user , token):
                    password = form.cleaned_data.get("new_password")
                    user.set_password(password)
                    print("پسورد هش شده:", user.password)
                    user.save()
                    messages.success(request , "رمز عبور باموفقیت تغییر کرد")
                    return redirect("account:user_login")
                else:
                    messages.error(request, "توکن معتبر نیست")
            except Member.DoesNotExist:
                messages.error(request, "کاربر یافت نشد")
            except Exception as e:
                messages.error(request, f"خطای سیستمی رخ داده است: {str(e)}")
        return render(request, self.template_name, {"form": form})




            



