from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.accounts.models import Account
from apps.profiles.models import Profile
from apps.transactions.methods import update_transaction_process
from apps.transactions.models import Transaction
from apps.transactions.tasks import create_transaction_async


# Create your views here.
class TransactionList(LoginRequiredMixin, ListView):
    template_name = "transaction/list.html"
    login_url = "/login/"
    context_object_name = "transactions"
    model = Transaction
    
    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Transaction List"
        return context

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return Transaction.objects.filter(user=profile)

class TransactionCreate(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = "transaction/create.html"
    login_url = "/login/"
    fields = ["from_account","to_account","amount","transaction_description"]
    success_url = reverse_lazy("transaction-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(user=self.request.user)

        context["page_title"] = "Create New Transaction"
        context["from_account"] = Account.objects.filter(profile=profile)
        return context


    def form_valid(self, form):
        transaction = form.save(commit=False)

        from_account = form.cleaned_data.get("from_account")
        amount = form.cleaned_data.get("amount")

        if from_account.current_balance < amount :
            form.add_error('amount', "Insufficient balance in the source account.")
            return self.form_invalid(form)

        transaction.transaction_status = 'pending'
        transaction.user = Profile.objects.get(user=self.request.user)
        transaction.save()

        create_transaction_async(transaction.id)
        
        return super().form_valid(form)