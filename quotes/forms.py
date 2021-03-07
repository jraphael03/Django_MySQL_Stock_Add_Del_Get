from django import forms
from .models import Stock

class StockForm(forms.ModelForm):       
    class Meta:
        model = Stock           # Name of the model you will be using
        fields = ["ticker"]     # Place all of the fields you will be placing inside of the database, (ticker found in models, and add_stock)