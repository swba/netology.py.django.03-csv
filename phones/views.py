from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request: WSGIRequest):
    match request.GET.get('sort', 'name'):
        case 'min_price':
            sort = 'price'
        case 'max_price':
            sort = '-price'
        case _:
            sort = 'name'
    phones = Phone.objects.all().order_by(sort)

    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    try:
        template = 'product.html'
        context = {
            'phone': Phone.objects.get(slug=slug)
        }
    except Phone.DoesNotExist:
        template = 'not_found.html'
        context = {}

    return render(request, template, context)
