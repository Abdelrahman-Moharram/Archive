from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("",views.index, name="index"),
    path("add-user/",views.addUser,name="add"),
    path("register/",views.register,name="register"),
    path("login/",views.user_login, name="login"),
    path("logout/",views.logout_user, name="logout"),
    path("edit/<str:militry_id>/",views.edit, name="edit"),
    path("delete/<str:militry_id>/",views.delete, name="delete"),
    path("<str:militry_id>/",views.profile, name="profile")
]

