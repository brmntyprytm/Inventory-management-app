from django.urls import path
from main.views import (
    show_main,
    create_weapon,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
    register,
    login_user,
    logout_user,
    increment,
    decrement,
    delete,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create_weapon/", create_weapon, name="create_weapon"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<int:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<int:id>/", show_json_by_id, name="show_json_by_id"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("increment/<int:id>/", increment, name="increment"),
    path("decrement/<int:id>/", decrement, name="decrement"),
    path("delete/<int:id>/", delete, name="delete"),
]
