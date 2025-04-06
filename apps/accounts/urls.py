from django.urls import path

from apps.accounts.views import AccountDashboard, AccountList, AccountCreate, AccountSearch

urlpatterns = [
    path("dashboard/", view=AccountDashboard.as_view(), name="dashboard"),
    path("account/list/",view=AccountList.as_view(),name="account-view"),
    path("account/new/",view=AccountCreate.as_view(),name="account-create"),
    path("account/search/",view=AccountSearch.as_view(),name="account-search"),
]