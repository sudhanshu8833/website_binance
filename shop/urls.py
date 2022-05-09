from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    path("", views.home, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("bots/", views.bots, name="bots"),
    path("error/", views.error, name="error"),
    path("signup", views.signup, name="signup"),
    path("handleLogin", views.handleLogin, name="handlelogin"),
    path("all_bots", views.all_bots, name="all_bots"),
    path("user_bots", views.user_bots, name="user_bots"),
    path("index", views.index, name="index"),
    path("settings", views.settings, name="settings"),
    path("checkout", views.checkout, name="checkout"),
    path("handleLogout", views.handleLogout, name="handleLogout"),
    path("withdraw", views.withdraw, name="withdraw"),
]