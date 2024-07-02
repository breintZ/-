from django import forms

from salon.models import Service, Category


class ServiceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Введите наименование услуги'
        }))
    category = forms.ModelChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-input',
            'placeholder': 'Выберите категорию услуги'
        }), queryset=Category.objects.all(), required=False)
    price = forms.DecimalField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Введите цену услуги'
        }))

    class Meta:
        model = Service
        fields = ('name', 'category', 'price')