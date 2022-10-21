from receipts.views import (
    receipt_list,
    create_receipt,
    account_list,
    category_list,
    create_category,
    create_account,
)
from django.urls import path


urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("accounts/", account_list, name="account_list"),
    path("categories/", category_list, name="category_list"),
    path("categories/create/", create_category, name="create_category"),
    path("accounts/create/", create_account, name="create_account"),
]
