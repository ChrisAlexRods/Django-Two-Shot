from django.shortcuts import render
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_receipt(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {"Receipt": receipt_list}
    return render(request, "receipts/detail.html", context)
