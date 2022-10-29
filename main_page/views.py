from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

import telebot
bot = telebot.TeleBot('5619814545:AAHWeh6Ts34UeQ4MDhWaPA5qSTsM_m9pl8Q')


def home_page(request):
    return render(request, 'main_page.html')


# получить все товары из базы и вывод
def get_all_products(request):
    all_products = models.Product.objects.all()
    return render(request, 'all_products.html', {'all_products': all_products})


def categories(request):
    all_categories = models.Category.objects.all()
    return render(request, 'index.html', {'all_categories': all_categories})


def get_exact_product(request, pk):
    current_product = models.Product.objects.get(product_name=pk)
    return render(request, 'current_product.html', {'current_product' : current_product})


def get_exact_category(request, pk):
    current_category = models.Category.objects.get(category_name=pk)
    category_products = models.Product.objects.filter(product_category=current_category)
    category_name = current_category
    return render(request, 'category_items.html', {'category_items' : category_products, 'category_name' : category_name})


def search_exact_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            models.Product.objects.get(product_name=get_product)
            return redirect(f'/product/{get_product}')
        except:
            return redirect('/')


def add_product_to_user_cart(request, pk):
    if request.method == 'POST':
        checker = models.Product.objects.get(product_name=pk)
        if checker.product_count >= int(request.POST.get('pr_count')):
            models.UserCart.objects.create(user_id=request.user.id,
                                           user_product=checker,
                                           user_product_quantity=request.POST.get('pr_count')).save()
            return redirect(f'/product/{pk}')
        else:
            return redirect(f'/product/{pk}')


def user_cart(request):
    cart = models.UserCart.objects.filter(user_id=request.user.id)
    return render(request, 'cart.html', {'cart_objects': cart})

def delete_exact_user_cart(request, pk):
    product_to_delete = models.Product.objects.get(product_name=pk)
    models.UserCart.objects.filter(user_id=request.user.id,
                                user_product=product_to_delete).delete()
    return redirect('/cart')

def zakaz(request):
    zakaz = models.UserCart.objects.filter(user_id=request.user.id)
    message = 'Новый заказ:\n'
    itog = 0
    for i in zakaz:
        message += f'{i.user_product.product_name} : {i.user_product_quantity} шт : {round(i.user_product_quantity*i.user_product.product_price)} сум\n'
        itog += i.user_product_quantity*i.user_product.product_price
    message += f'На общую сумму в {round(itog)} сум'
    bot.send_message(609805881, message)
    models.UserCart.objects.filter(user_id=request.user.id).delete()
    return render(request, 'zakaz.html')







