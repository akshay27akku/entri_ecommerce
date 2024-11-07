from django import forms

from home.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_control', 'placeholder': "Name of the product"}),
            'description': forms.Textarea(attrs={'class': 'form_control', 'placeholder': "Description"}),
            'price': forms.NumberInput(attrs={'class': 'form_control', 'placeholder': "Price of the product"}),
            'category': forms.Select(attrs={'class': 'form_control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form_control'}),
            # 'available': forms.BooleanInput(attrs={'class': 'form_control'}),
            'stock': forms.NumberInput(attrs={'class': 'form_control', 'placeholder': "stock"}),
        }
