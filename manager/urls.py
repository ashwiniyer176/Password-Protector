from django.urls import path
from manager import views

app_name = "manager"
urlpatterns = [
    path("", views.showData, name="home"),
    path("newPassword/", views.addNewPassword, name="newPassword"),
    path('editPassword/<int:itemID>/', views.editPassword, name="editPassword"),
    path('deletePassword/<int:itemID>',
         views.deletePassword, name="deletePassword")
]
