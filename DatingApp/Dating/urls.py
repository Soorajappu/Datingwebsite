from django.urls import path
from . import views

app_name = 'dating'
urlpatterns = [
    path('', views.UserCreateView.as_view(), name='user_create'),
    path('details/', views.DetailCreateView.as_view(), name='details_create'),
    path('employment/', views.EmploymentView.as_view(), name='employment'),
    path('relationship/', views.RelationshipView.as_view(), name='relationship'),
    path('home/', views.HomeView.as_view(), name='home'),
]