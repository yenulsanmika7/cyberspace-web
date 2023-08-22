from django.urls import path
from base.views import order_views as views

urlpatterns = [
    path('', views.getOrders, name='orders'), 
    path('add/', views.addOrderItems, name='orders-add'), 
    path('my-orders/', views.getMyOrders, name='my-orders'), 

     path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),
     
    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),        
]
