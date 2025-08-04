from django.urls import path , re_path
from .views import HomeView , ContactView, PortfolioDetailView 

app_name = 'home'

urlpatterns = [
    
    path('contact/', ContactView.as_view(), name='contact'),
    re_path(r'^(?P<cat_slug>[-\wآ-ی]+)/$', HomeView.as_view() , name='home'),
    re_path(r'^portfolio/(?P<port_slug>[-\wآ-ی]+)/$', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('', HomeView.as_view() , name='home'),

]