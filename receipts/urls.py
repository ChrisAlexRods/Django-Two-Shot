from receipts.views import (
    receipt_list,
    create_receipt,
    account_list,
    category_list,
)
from django.urls import path, include


urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("accounts/", account_list, name="account_list"),
    path("categories/", category_list, name="category_list"),
]
