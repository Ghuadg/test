
from django.http import HttpResponse
from django.shortcuts import render, redirect
import telebot
import os

from .models import Product, Review

from .config import BOT_TOKEN, CHAT_ID

bot = telebot.TeleBot(BOT_TOKEN)
# Create your views here.

def home(request):
    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(name__contains=search).all()
    else:
        products = Product.objects.all()

    return render(request, "index.html", {
        'products': products,
        'products_found': len(products) > 0,
        'search': search if search else '',
    })

def view_product(request, id):
    product = Product.objects.filter(id=id).first()


    if request.method == "POST":
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        usage_duration = request.POST.get('duration')
        text = request.POST.get('review')

        review = Review(
            product=product,
            author=author,
            rating=rating,
            usage_duration=usage_duration,
            text=text,
        )
        review.save()

    reviews = product.review_set.all()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews,
    })

def payment(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        number = request.POST.get('number')
        # Send message to Telegram
        bot.send_message(CHAT_ID, f'''📦 Новый заказ: {product.name}
💸 Цена: {product.price} рублей
ФИО покупателя: {name}
Адрес доставки: {address}
Номер телефона покупателя для связи: {number}
''')
        return redirect('/paymentend')

    return render(request, "payment.html", {
        'product': product
    })



def aboutus(request):
    return render(request, "aboutus.html")

def productlist(request):
    return render(request, "productlist.html")

def profile(request):
    return render(request, "profile.html")

def paymentend(request):
    return render(request, "paymentend.html")

def delivery(request):
    return render(request, "delivery.html")

from django.http import JsonResponse
from .models import Product

def autocomplete(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(name__icontains=query).values('name')
        suggestions = [product['name'] for product in products]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)

