from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('make_order/', MakeOrder.as_view(), name='make_order'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', login_required(LogoutView.as_view(next_page="/"), login_url='login'), name='logout'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('order/<int:id_order>/detail', login_required(OrderDetail.as_view(), login_url='login'),
         name='order_detail'),
    path('order/<int:id_order>/delete', login_required(OrderDelete.as_view(), login_url='login'),
         name='order_delete'),
    path('order/<int:id_order>-<int:id_jeweller>/accept', login_required(OrderAccept.as_view(), login_url='login'),
         name='order_accept'),
    path('products/', CompletedProducts.as_view(), name='completed_product'),
]