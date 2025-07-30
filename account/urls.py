from django.urls import  path , re_path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterView.as_view() , name='user_register'),
    path('login/', views.LoginView.as_view() , name='user_login'),
    path('logout/', views.LogoutView.as_view() , name='user_logout'),
    path('profile/', views.EditProfileView.as_view() , name='user_profile'),
    path('forget_password/', views.ForgetPasswordView.as_view(), name="forget_password"),
    path('reset_password/<uidb64>/<token>/', views.ResetPasswordView.as_view(), name="reset_password_form"),
]