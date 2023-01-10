from django.urls import path
from .views import register,profile,user_detail
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name= 'login'),
    path('profile/', profile, name = 'profile'),
    path('detail/<int:pk>', user_detail, name='user-detail')
]