from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ecommerce.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/index.html', context={"products": products})


def productdetail(request, slug):
    product=get_object_or_404(Product,slug=slug)
    #return HttpResponse(f"{product.name}:{product.price}")
    return render(request,'ecommerce/detail.html',context={"product":product})
