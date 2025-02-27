import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def load_from_json(file_name):
    with open(os.path.join(settings.BASE_DIR, f'mainapp/json/{file_name}.json'), encoding='UTF-8') as f:
        return json.load(f)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for cat in categories:
            ProductCategory.objects.create(**cat)

        products = load_from_json('products')

        Product.objects.all().delete()
        for prod in products:
            _cat = ProductCategory.objects.get(name=prod['category'])
            prod['category'] = _cat
            Product.objects.create(**prod)

        try:
            ShopUser.objects.get(username='django').delete()
        except:
            pass
        finally:
            ShopUser.objects.create_superuser('django', 'su', 'geekbrains', age=20) 
