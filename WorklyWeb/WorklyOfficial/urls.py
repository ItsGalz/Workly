from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # URL principal es HOME
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

     # ✅ NUEVAS RUTAS PARA EL FRONTEND
    path('memberships/', views.memberships_view, name='memberships'),
    
]