from receipts.views import list_receipt
from django.urls import path, include


urlpatterns = [path("", list_receipt, name="home")]
