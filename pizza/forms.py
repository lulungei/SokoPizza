from django import forms

class OrderForm(forms.Form):
    order = forms.CharField(label='Order', widget=forms.Textarea)