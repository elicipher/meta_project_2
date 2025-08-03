from django.urls import path , re_path
from .views import HomeView , ContactView, PortfolioView

app_name = 'home'

urlpatterns = [
    
    path('contact/', ContactView.as_view(), name='contact'),
    path('<slug:cat_slug>/', HomeView.as_view() , name='home'),
    re_path(r'^portfolio/(?P<port_slug>[-\wآ-ی]+)/$', PortfolioView.as_view(), name='portfolio-detail'),
    path('', HomeView.as_view() , name='home'),

]