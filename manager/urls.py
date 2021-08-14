from django.urls import path
from .views import showData, addNewPassword, editPassword

app_name = "manager"
urlpatterns = [
    path("", showData, name="home"),
    path("newPassword/", addNewPassword, name="newPassword"),
    path('editPassword/<int:itemID>/', editPassword, name="editPassword")
]
