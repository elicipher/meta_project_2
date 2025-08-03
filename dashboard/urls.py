from django.urls import path , include
from . import views

app_name = 'dashboard'
home_urls = [

    path('about-us/edit/',views.AboutUsUpdateView.as_view(),name="edit_about"),

    path('service/list/',views.ServiceListView.as_view(),name="service_list"),
    path('service/create/',views.ServiceCreateView.as_view(),name="service_create"),
    path('service/delete/<int:pk>/',views.ServiceDeleteView.as_view(),name="service_delete"),
    path('service/update/<int:pk>/',views.ServiceUpdateView.as_view(),name="service_update"),

    path('stats-section/list/', views.StatsSectionListView.as_view(),name='stats_list'),
    path('stats-section/create/', views.StatsSectionCreateView.as_view(),name='stats_create'),
    path('stats-section/delete/<int:pk>/', views.StatsSectionDeleteView.as_view(),name='stats_delete'),
    path('stats-section/update/<int:pk>/', views.StatsSectionUpdateView.as_view(),name='stats_update'),

    path('portfolio_list/',views.PortfolioListView.as_view(),name = 'portfolio_list'),
    path('portfolio/create/',views.PortfolioCreateView.as_view(),name = 'portfolio_create'),
    path('portfolio/delete/<int:pk>/',views.PortfolioDeleteView.as_view(),name = 'portfolio_delete'),
    path('portfolio/update/<int:pk>/',views.PortfolioUpdateView.as_view(),name = 'portfolio_update'),

    path('portfolio_category_list/',views.PortfolioCategoryListView.as_view(), name = 'portfolio_category_list'),
    path('portfolio_category_create/',views.PortfolioCategoryCreateView.as_view(), name = 'portfolio_category_create'),
    path('portfolio_category_delete/<int:pk>/',views.PortfolioCategoryDeleteView.as_view(), name = 'portfolio_category_delete'),
    path('portfolio_category_update/<int:pk>/',views.PortfolioCategoryUpdateView.as_view(), name = 'portfolio_category_update'),

    
    path('team_list/',views.TeamMemberListView.as_view(), name = 'team_list'),
    path('team_create/',views.TeamMemberCreateView.as_view(), name = 'team_create'),
    path('team_delete/<int:pk>/',views.TeamMemberDeleteView.as_view(), name = 'team_delete'),
    path('team_update/<int:pk>/',views.TeamMemberUpdateView.as_view(), name = 'team_update'),

    
    path('contact_list/',views.ContactListView.as_view(), name='contact_list'),
    path('contact_reply/<int:pk>/',views.ContactReplyView.as_view(), name='contact_reply'),
    path('contact_delete/<int:pk>/',views.ContactDeleteView.as_view(), name='contact_delete'),

    
]


urlpatterns = [

    path('home/app/', include(home_urls)),
    path('',views.DashboardView.as_view(),name="dashboard"),

]