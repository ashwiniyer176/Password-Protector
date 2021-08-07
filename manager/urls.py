from django.urls import path
from .views import showData, addNewPassword

app_name = "manager"
urlpatterns = [
    path("", showData, name="home"),
    path("newPassword/", addNewPassword, name="newPassword")
]
