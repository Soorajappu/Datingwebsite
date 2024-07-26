from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.UserCreateView.as_view(), name='register'),
    path('home/', views.HomeView.as_view(), name='home'),
]