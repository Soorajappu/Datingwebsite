from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup', views.UserCreateView.as_view(), name='register'),
    path('register-detail/', views.RegisterBasicDetailView.as_view(), name='register_detail'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('employment/', views.EmploymentView.as_view(), name='employment'),
    path('employer-detail/', views.EmployerDetailView.as_view(), name='employer_detail'),
    path('jobseeker/', views.JobSeekerDetailView.as_view(), name='jobseeker'),
    path('relationship/', views.RelationshipView.as_view(), name='relationship'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
]