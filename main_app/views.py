import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
from django.views import View


class MainPage(View):

    def get(self, request, *args, **kwargs):
        products = CompletedProduct.objects.all()[:5]
        context = {
            'products': products,
        }
        return render(request, 'main_app/index.html', context)


class MakeOrder(View):

    def get(self, request, *args, **kwargs):
        form = MakeOrderForm(request.POST or None)
        context = {
            'form': MakeOrderForm
        }
        return render(request, 'main_app/make_order.html', context)

    def post(self, request, *args, **kwargs):
        form = MakeOrderForm(request.POST or None)
        if form.is_valid():
            PIB = form.cleaned_data['PIB']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            type_of_jewellery = form.cleaned_data['type_of_jewellery']
            delivery = form.cleaned_data['delivery']
            broadcast = form.cleaned_data['broadcast']
            order_datetime = datetime.datetime.now()
            Order.objects.create(
                PIB=PIB,
                phone_number=phone_number,
                address=address,
                type_of_jewellery=type_of_jewellery,
                delivery=delivery,
                broadcast=broadcast,
                order_datetime=order_datetime
            )
            get_id = Order.objects.get(PIB=PIB,
                                       phone_number=phone_number,
                                       address=address,
                                       type_of_jewellery=type_of_jewellery,
                                       delivery=delivery,
                                       broadcast=broadcast,
                                       order_datetime=order_datetime
                                       )
            context = {
                'id': get_id.id
            }
            return render(request, 'main_app/success.html', context)
        return HttpResponseRedirect('/make_order')


class Login(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            form = LoginForm(request.POST or None)
            context = {
                'form': form
            }
            return render(request, 'main_app/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'main_app/login.html', context)


class OrdersView(View):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        context = {
            'orders': orders
        }
        return render(request, 'main_app/orders.html', context)


class OrderDetail(View):

    def get(self, request, *args, **kwargs):
        id_order = kwargs.get('id_order')
        order = Order.objects.get(id=id_order)
        jeweller = Jeweller.objects.all()
        context = {
            'order': order,
            'jewellers': jeweller
        }
        return render(request, 'main_app/order_detail.html', context)


class OrderDelete(View):

    def get(self, request, *args, **kwargs):
        id_order = kwargs.get('id_order')
        order = Order.objects.get(id=id_order)
        order.delete()
        return HttpResponseRedirect('/orders')


class OrderAccept(View):

    def get(self, request, *args, **kwargs):
        id_order = kwargs.get('id_order')
        id_jeweller = kwargs.get('id_jeweller')
        order = Order.objects.get(id=id_order)
        order.fk_jeweller_id = id_jeweller
        order.save()

        return HttpResponseRedirect('/orders')


class CompletedProducts(View):

    def get(self, request, *args, **kwargs):
        products = CompletedProduct.objects.all()
        context = {
            'products': products
        }
        return render(request, 'main_app/completed_products.html', context)

    def post(self, request, *args, **kwargs):
        form = CompletedProductsForm(request.POST or None)
        if form.is_valid():
            pass
        pass


class CompletedProductsDetail(View):

    def get(self, request, *args, **kwargs):
        id_product = kwargs.get('id_product')
        product = CompletedProduct.objects.get(id=id_product)
        context = {
            'product': product
        }
        return render(request, 'main_app/completed_products_detail.html', context)
