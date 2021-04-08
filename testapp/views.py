from .models import Product
from django.db import connection
from django.http import HttpResponse
from random import randrange


def product_view(request):
    rand_num = randrange(0, 2_000_000)
    _ = Product.objects.get(attributes__name=rand_num)
    dict_lookup_time = connection.queries[-1]["time"]
    _ = Product.objects.get(
        attributes__values__contains=[rand_num, rand_num + 1],
    )
    list_lookup_time = connection.queries[-1]["time"]
    return HttpResponse(
        f"dict lookup time: {dict_lookup_time} "
        f"list lookup time: {list_lookup_time}"
    )
