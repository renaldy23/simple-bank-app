from django.urls import path

from apps.transactions.views import TransactionList, TransactionCreate

urlpatterns = [
    path("transaction/list/",view=TransactionList.as_view(),name="transaction-list"),
    path("transaction/create",view=TransactionCreate.as_view(),name="transaction-create"),
]