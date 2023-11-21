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
    edit_product,
    get_product_json,
    add_product_ajax,
    delete_product_ajax,
    create_product_flutter,
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
    path("edit/<int:id>/", edit_product, name="edit_product"),
    path("get-product/", get_product_json, name="get_product_json"),
    path("create-product-ajax/", add_product_ajax, name="add_product_ajax"),
    path(
        "delete-product-ajax/<int:id>", delete_product_ajax, name="delete_product_ajax"
    ),
    path("create-flutter/", create_product_flutter, name="create_product_flutter"),
]
