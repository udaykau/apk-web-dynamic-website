from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('product/<int:sno>/<str:gender>', views.product, name='product'),
    path('shop/<str:gender>/<str:category>', views.shop, name='shop'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('Error404', views.Error404, name='Error404'),
    path('Order_Complete', views.Order_Complete, name='Order_Complete'),
    path('Order_Uncomplete', views.Order_Uncomplete, name='Order_Uncomplete'),
    path('Cart', views.Cart, name='Cart'),
    path('contact', views.contact, name='contact'),
    path('Checkout', views.Checkout, name='Checkout'),
    path('privacy_Policy', views.privacy_Policy, name='privacy_Policy'),
    path('faq', views.faq, name='faq'),
    path('TermsandCondition', views.TermsandCondition, name='TermsandCondition'),
    path('ComingSoon', views.ComingSoon, name='ComingSoon'),
    path('Shop/<str:category>', views.Shop, name='Shop'),
    path('Search', views.Search, name='Search'),
    ]
