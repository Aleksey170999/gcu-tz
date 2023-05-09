from django.core.management.base import BaseCommand

from apps.catalog.models import Category, Product
from apps.accounts.models import User


class Command(BaseCommand):
    """
    Заполнение БД
    """

    def handle(self, *args, **options) -> None:
        Product.objects.all().delete()
        Category.objects.all().delete()
        User.objects.all().delete()

        manager1 = User.objects.create_user(username='manager1',
                                            email="manager1@manager.com",
                                            password='manager123',
                                            is_manager=True)

        manager2 = User.objects.create_user(username='manager2',
                                            email="manager@manager.com",
                                            password='manager123',
                                            is_manager=True)

        cat1 = Category.objects.create(title='Category_1',
                                       manager=manager1)
        cat2 = Category.objects.create(title='Category_2',
                                       manager=manager2)

        Product.objects.create(title='test1',
                               price='10000',
                               category=cat1,
                               description='test description',
                               article='111111')
        Product.objects.create(title='test2',
                               price='20000',
                               category=cat1,
                               description='test description',
                               article='222222')

        Product.objects.create(title='test3',
                               price='30000',
                               category=cat1,
                               description='test description',
                               article='333333')

        Product.objects.create(title='test4',
                               price='40000',
                               category=cat2,
                               description='test description',
                               article='444444')
        Product.objects.create(title='test5',
                               price='50000',
                               category=cat2,
                               description='test description',
                               article='555555')
        Product.objects.create(title='test6',
                               price='60000',
                               category=cat2,
                               description='test description',
                               article='666666')
