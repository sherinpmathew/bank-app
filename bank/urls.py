from django.urls import path
from.views import AccountCreateView,SigninView,BalanceView,FundTransferView,PaymentHistoryView,SignOutView,TransactionFilterView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
urlpatterns=[
    path("login",SigninView.as_view(),name="signin"),
    path("register",AccountCreateView.as_view(),name="register"),
    path("home",login_required(TemplateView.as_view(template_name="home.html"),login_url="signin"),name="home"),
    path("balance",BalanceView.as_view(),name="balance"),
    path("transactions",FundTransferView.as_view(),name="transaction"),
    path("logout",SignOutView.as_view(),name="signout"),
    path("payhistory",PaymentHistoryView.as_view(),name="payhistory"),
    path("filter",TransactionFilterView.as_view(),name="filter"),
    ]