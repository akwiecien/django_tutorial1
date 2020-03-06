from django.urls import path
from .views import home, add_country
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home', home, name="world_home"),
    path('login', LoginView.as_view(template_name='world/login_page.html'), name='world_login'),
    path('logout', LogoutView.as_view(), name='world_logout'),
    path('add_country', add_country, name='world_add_country')
]