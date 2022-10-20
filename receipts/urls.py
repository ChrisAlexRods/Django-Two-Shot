from receipts.views import list_receipt, create_receipt
from django.urls import path, include


urlpatterns = [
    path("", list_receipt, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]
