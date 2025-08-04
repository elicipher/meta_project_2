from django import forms
from .models import Member
from django.core.exceptions import ValidationError 
from django.contrib.auth import authenticate



class UserRegitrationForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "single-field",
            "placeholder": "نام و نام خانوادگی"
        })
    )
    phone_number = forms.CharField(
        label='شماره تلفن',
        max_length=11,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "single-field",
            "placeholder": 'شماره تلفن'
        })
    )
    email = forms.EmailField(
        label='ایمیل',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "single-field",
            "placeholder": 'ایمیل'
        })
    )
    password = forms.CharField(
        label='رمز عبور',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "single-field",
            "placeholder": "رمز عبور"
        })
    )
    confirm_password = forms.CharField(
        label='تایید رمز عبور',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "single-field",
            "placeholder": "تایید رمز عبور"
        })
    )

    def clean(self):
        cd = super().clean()

        # full_name
        full_name = cd.get("full_name")
        if not full_name:
            self.add_error("full_name", "لطفا نام و نام خانوادگی را وارد کنید")

        # phone_number
        phone_number = cd.get("phone_number")
        if not phone_number:
            self.add_error("phone_number", "لطفا شماره تلفن را وارد کنید")
        elif Member.objects.filter(phone_number=phone_number).exists():
            self.add_error("phone_number", "شماره تلفن درحال حاضر وجود دارد")

        # email
        email = cd.get("email")
        if not email:
            self.add_error("email", "لطفا ایمیل را وارد کنید")
        elif Member.objects.filter(email=email).exists():
            self.add_error("email", "این ایمیل قبلاً ثبت شده است")

        # password
        password = cd.get("password")
        confirm_password = cd.get("confirm_password")
        if not password:
            self.add_error("password", "لطفا رمز عبور را وارد کنید")
        elif not confirm_password:
            self.add_error("confirm_password", "لطفاً تایید رمز را وارد کنید")
        elif confirm_password != password:
            self.add_error("confirm_password", "رمزهای عبور باید مطابقت داشته باشند")
        elif len(password) <= 8:
            self.add_error("password", "رمز عبور باید بیشتر از ۸ کاراکتر باشد")

        cd.pop("confirm_password", None)
        return cd


        
class UserLoginForm(forms.Form):
    phone_number = forms.CharField(label='شماره تلفن',max_length=11,required=False , widget=forms.TextInput(attrs={ "class": "single-field","placeholder": " شماره تلفن تان را وارد کنید  "})) 
    password = forms.CharField(label='رمز عبور' ,required=False , widget=forms.TextInput(attrs={ "class": "single-field","placeholder": "رمز عبور"}))

    def clean(self):
        cd = super().clean()
        phone_number = cd.get("phone_number")
        password= cd.get("password")
        user = authenticate(username = phone_number , password =password )
       
        if not password or not phone_number  :
            raise ValidationError("لطفا فرم را پر کنید")
        if user is None :
            raise ValidationError("شماره تلفن یا رمز عبور اشتباه است")

        self.user = user  # کاربر معتبر را ذخیره می‌کنیم تا در ویو استفاده شود
        
        return cd
    
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('avatar','full_name','email',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
            
        }
        labels = {
            'email': ':ایمیل',
            'full_name':  ':نام',
            'avatar': ' :تصویر پروفایل',
        }
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل",required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ایمیل خود را وارد کنید"})
    )
    def clean(self):
        
        cd = super().clean()
        email = cd.get('email')
        email_exists = Member.objects.filter(email = email).exists()
        if not email : 
            raise ValidationError("لطفا فرم را پر کنید")
        elif not email_exists :
            raise ValidationError("لطفا ایمیل معتبر وارد کنید")
        return cd

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label="رمز عبور جدید" , required= False ,widget=forms.TextInput(attrs={ "class": "single-field","placeholder":"رمز عبور جدید"}))
    confirm_password = forms.CharField(label="تایید رمز عبور",required= False ,widget=forms.TextInput(attrs={"class":"single-field", "placeholder":"تایید رمز عبور"}))

    def clean(self):
        cd = super().clean()
        password = cd.get("new_password")
        confirm_password = cd.get("confirm_password")
        if not password or not confirm_password:
            raise ValidationError("لطفا فرم را پر کنید")
        elif len(password) <= 8 :
            raise ValidationError("رمز عبور باید بیشتر از ۸ تا کارکتر باشد")
        elif password != confirm_password :
            raise ValidationError("رمز های عبور باید باهم مطابقت داشته باشند")
        
        cd.pop("confirm_password", None)
        return cd 
    


        






        