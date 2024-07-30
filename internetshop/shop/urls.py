from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("product/<int:id>", views.view_product, name="view_product"),
    path("payment/<int:id>", views.payment, name='payment'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('productlist', views.productlist, name='productlist'),
    path('profile', views.profile, name='profile')
]