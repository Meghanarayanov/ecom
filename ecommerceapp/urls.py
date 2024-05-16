from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('logout',views.logout,name='logout'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addproduct',views.addproduct,name='addproduct'),

    path('loginform',views.loginform,name='loginform'),
    path('userindex',views.userindex,name='userindex'),
    path('signupform',views.signupform,name='signupform'),
    path('addcategory_db',views.addcategory_db,name='addcategory_db'),
    path('addproduct_db',views.addproduct_db,name='addproduct_db'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('deleteproduct/<int:pk>',views.deleteproduct,name='deleteproduct'),
    path('viewuser',views.viewuser,name='viewuser'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),

    path('category_page/<str:category_name>/', views.category_page, name='category_page'),
    path('mencategory', views.mencategory, name='mencategory'),
    path('womencategory', views.womencategory, name='womencategory'),
    path('boycategory', views.boycategory, name='boycategory'),
    path('girlcategory', views.girlcategory, name='girlcategory'),
    path('addtocart/<int:pk>', views.addtocart, name='addtocart'),
    path('cart', views.cart, name='cart'),
    path('decrease/<int:pk>', views.decrease, name='decrease'),
    path('increase/<int:pk>', views.increase, name='increase'),
    path('remove/<int:pk>', views.remove, name='remove'),
    path('checkout', views.checkout, name='checkout'),
    













 


   
]