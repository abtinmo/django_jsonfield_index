from django.core.management.base import BaseCommand
from testapp.models import Product
from itertools import islice


class Command(BaseCommand):

    def handle(self, *args, **options):
        batch_size = 5000
        objs = (
            Product(
                name='product No.%s' % i,
                attributes={"name": i, "values": [i, i + 1]},
            ) for i in range(2_000_000)
        )
        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            Product.objects.bulk_create(batch, batch_size)
