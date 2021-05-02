from django.forms import ModelForm
from .models import CustomerOrder

class CustomerOrderForm(ModelForm):
    class Meta:
        model = CustomerOrder
        fields = "__all__"