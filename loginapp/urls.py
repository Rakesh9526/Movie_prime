from django.urls import path
from . import views
app_name='loginapp'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile_modal/', views.view_profile_modal, name='profile_modal'),
]