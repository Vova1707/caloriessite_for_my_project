from django.shortcuts import render
from .models import Listofproducts, ViewProduct


def index(request):
    bbs = Listofproducts.objects.order_by('name_product')
    dict_1 = {'bbs': bbs}
    return render(request, 'mainmenu/index.html', dict_1)

def about(request):
    return render(request, 'mainmenu/about.html')

def product(request):
    product_rublic = ViewProduct.objects.all()
    dict_2 = {'products': product_rublic}
    return render(request, 'mainmenu/product.html', dict_2)

def func_of_viewproduct(request, product_id):
    currect_rublic = ViewProduct.objects.get(pk=product_id)
    bbs = Listofproducts.objects.filter(rubric=currect_rublic)
    dict_3 = {'product': currect_rublic, 'bbs': bbs}
    return render(request, 'mainmenu/for_rublic.html', dict_3)
