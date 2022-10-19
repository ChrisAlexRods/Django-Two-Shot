from django.shortcuts import render
from receipts.models import ExpenseCategory, Account, Receipt

# Create your views here.


def list_receipt(request):
    receipt_list = Receipt.objects.all()
    context = {"Receipt": receipt_list}
    return render(request, "receipts/detail.html", context)
