from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.UserCreateView.as_view(), name='register'),
    path('register-detail/', views.RegisterBasicDetailView.as_view(), name='register_detail'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
]