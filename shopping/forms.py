from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 18)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoicesField(
        choices= PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )

    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)