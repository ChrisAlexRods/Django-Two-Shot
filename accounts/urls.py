from accounts.views import login_user
from django.urls import path, include

urlpatterns = [path("login/", login_user, name="login")]
