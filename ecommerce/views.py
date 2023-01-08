from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ecommerce.models import Product, Cart, Order


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/index.html', context={"products": products})


def productdetail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # return HttpResponse(f"{product.name}:{product.price}")
    return render(request, 'ecommerce/detail.html', context={"product": product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    carte, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,
                                                 ordered=False,
                                                 product=product)

    if created:
        carte.orders.add(order)
        carte.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    cart1 = get_object_or_404(Cart, user=request.user)
    return render(request, 'ecommerce/cart.html', context={"orders": cart1.orders.all()})


def delete_cart(request):
    if cart1 := request.user.cart:
        # cart1.orders.all().delete()
        cart1.delete()

    return redirect('index')
