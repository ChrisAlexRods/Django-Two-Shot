from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm

# Create your views here.


@login_required
def receipt_list(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {"Receipt": receipt_list}
    return render(request, "receipts/list.html", context)


@login_required
def account_list(request):
    account_list = Account.objects.filter(owner=request.user)
    context = {"Accounts": account_list}
    return render(request, "accounts/list.html", context)


@login_required
def category_list(request):
    category_list = ExpenseCategory.objects.filter(owner=request.user)
    context = {"Categories": category_list}
    return render(request, "categories/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

        context = {
            "form": form,
        }
        return render(request, "receipts/create.html", context)
