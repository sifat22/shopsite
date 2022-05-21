from.models import Product,Category
from django.shortcuts import render,get_object_or_404

# Create your views here.

def store(request,category_slug=None):
    categories=None
    products=None 

    if category_slug !=None:
        categories = get_object_or_404(Category,slug=category_slug)
        store=Product.objects.filter(category=categories,is_available=True)
        product_count=store.count()

    else:
        store=Product.objects.all().filter(is_available=True)
        product_count=store.count()

    return render(request,'store/store.html',{
        'store':store,
        'count':product_count
    })


def product_details(request,category_slug,product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e


    return render(request,'store/product_detail.html',{
        'single_product':single_product
    });
   