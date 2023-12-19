from django import forms
from django.contrib.auth.models import User
from .models import Order, CompletedProduct


class MakeOrderForm(forms.ModelForm):
    PIB = forms.CharField(required=True, max_length=90, label='ПІБ')
    phone_number = forms.CharField(required=True, max_length=45, label='Номер телефону')
    address = forms.CharField(required=True, max_length=90, label='Адреса')
    type_of_jewellery = forms.CharField(required=True, max_length=45, label='Тип прикраси')
    delivery = forms.ChoiceField(choices=Order.delivery_choices, required=True, label='Доставка')
    broadcast = forms.ChoiceField(choices=Order.broadcast_choices, required=True, label='Трансляція')

    def clean(self):
        PIB = self.cleaned_data['PIB']
        phone_number = self.cleaned_data['phone_number']
        address = self.cleaned_data['address']
        type_of_jewellery = self.cleaned_data['type_of_jewellery']
        delivery = self.cleaned_data['delivery']
        broadcast = self.cleaned_data['broadcast']
        return self.cleaned_data

    class Meta:
        model = Order
        fields = ('PIB', 'phone_number', 'address', 'type_of_jewellery', 'delivery', 'broadcast')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логін'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Неправильний логін або пароль!')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неправильний логін або пароль!')
        return self.cleaned_data

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class CompletedProductsForm(forms.ModelForm):
    class Meta:
        model = CompletedProduct
        fields = (
            'name',
            'amount',
            'size',
            'price',
            'state',
            'image',
            'order',
        )
