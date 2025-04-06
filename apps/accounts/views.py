from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from .models import Account
from ..profiles.models import Profile
from .utils import generate_unique_account_number
from django.http import JsonResponse


# Create your views here.
class AccountDashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(user=self.request.user)
        context["current_date"] = datetime.now().strftime("%A, %B %d, %Y")
        context["profile"] = profile
        return context


class AccountList(LoginRequiredMixin, ListView):
    model = Account
    template_name = "account/list.html"
    login_url = "/login/"
    context_object_name = "accounts"

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        account = Account.objects.filter(profile=profile)

        if not account:
            return None

        return account

    def get_context_data(
            self, *, object_list=..., **kwargs
    ):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Account List"
        return context


class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "account/create.html"
    login_url = "/login/"
    fields = ["identity_number", "tax_number", "card_holder_name", "card_name","current_balance","currency","account_purpose"]
    success_url = reverse_lazy("account-view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create New Bank Account"
        return context

    def form_valid(self, form):
        account = form.save(commit=False)
        account.profile = Profile.objects.get(user=self.request.user)
        account.account_number = generate_unique_account_number()
        account.save()

        return super().form_valid(form)


class AccountSearch(View):
    def get(self, request, *args, **kwargs):
        account_number = request.GET.get("account_number")
        try:
            account = Account.objects.get(account_number=account_number)
            return JsonResponse({
                'success': True,
                'account_holder': account.card_holder_name,
                'account_number': account.account_number,
                'account_id': account.id,
            })
        except Account.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Account not found'})