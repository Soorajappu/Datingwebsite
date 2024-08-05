from django.urls import path
from . import views

app_name = 'dating'
urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]