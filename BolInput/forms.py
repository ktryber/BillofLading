from django import forms
from .models import Load

class LoadForm(forms.ModelForm):

    class Meta:
        model = Load
        fields = ('load_number', 'carrier','pickup_date', 'delivery_date', 'shipper', 
        'consignee', 'po_number', 'pu_number', 'pieces', 'description')