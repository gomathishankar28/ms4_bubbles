from django.shortcuts import render, get_object_or_404
from products.models import Product


def index(request):
    """ A view to return the index page """

    latest_arrival_1 = get_object_or_404(Product, pk=6)
    latest_arrival_2 = get_object_or_404(Product, pk=64)
    latest_arrival_3 = get_object_or_404(Product, pk=65)

    template = 'home/index.html'
    context = {
        'latest_arrival_1': latest_arrival_1,
        'latest_arrival_2': latest_arrival_2,
        'latest_arrival_3': latest_arrival_3,
    }

    return render(request, template, context)