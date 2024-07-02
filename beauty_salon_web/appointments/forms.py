from django import forms

from appointments.models import DateTable, TimeTable, Sale
from users.models import User


class DateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'input-form',
            'placeholder': 'Введите дату'
        }
    ))

    class Meta:
        model = DateTable
        fields = ('date', )


class TimeForm(forms.ModelForm):
    date = forms.ModelChoiceField(widget=forms.Select(
        attrs={
            'class': 'input-form',
            'placeholder': 'Выберите дату'
        }
    ), queryset=DateTable.objects.all())
    time_start = forms.TimeField(widget=forms.TimeInput(
        attrs={
            'class': 'input-form',
            'placeholder': 'Введите начало периода'
        }

    ))
    time_end = forms.TimeField(widget=forms.TimeInput(
        attrs={
            'class': 'input-form',
            'placeholder': 'Введите конец периода'
        }
    ))

    class Meta:
        model = TimeTable
        fields = ('date', 'time_start', 'time_end')


class SaleForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input-form',
            'placeholder': 'Введите название скидки'
        }
    ))
    percent = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'input-form',
            'placeholder': 'Введите процент скидки (в процентах)'
        }
    ))
    user = forms.ModelChoiceField(widget=forms.Select(
        attrs={
            'class': 'input-form',
            'placeholder': 'Выберите дату'
        }
    ), queryset=User.objects.filter(is_superuser=False))

    class Meta:
        model = Sale
        fields = ('name', 'percent', 'user')