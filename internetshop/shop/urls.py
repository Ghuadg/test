from django.urls import path
from . import views
from .views import home, autocomplete

urlpatterns = [
    path('', views.home, name='home'),
    path("product/<int:id>", views.view_product, name="view_product"),
    path("payment/<int:id>", views.payment, name='payment'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('productlist', views.productlist, name='productlist'),
    path('profile', views.profile, name='profile'),
    path('paymentend', views.paymentend, name='paymentend'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('delivery', views.delivery, name='delivery')

]


