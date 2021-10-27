from django.urls import path

from .views import register, login_user, logout_user, dashboard, create_wallet

app_name = "accounts"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('verify/', create_wallet, name='verify')
]
