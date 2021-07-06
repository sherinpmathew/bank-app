import django_filters
from.models import Transactions
class transactionFilter(django_filters.FilterSet):
    class Meta:
        Model=Transactions
        fields=["date","amount","from_account_number","to_account_number"]