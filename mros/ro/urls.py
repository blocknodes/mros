from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
#    path('login/', views.loginPage, name="login"),  
#    path('logout/', views.logoutUser, name="logout"),
#    path('orders/', views.index, name='orders'),
#    path('orders/create/', views.createOrder, name='createOrder'),
    ]
