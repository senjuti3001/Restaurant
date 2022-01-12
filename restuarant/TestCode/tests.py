from django.test import TestCase

from restuarant.model.models import Menu, Category


# Create your tests here.
# class IndexTest(TestCase):
#     def test_model_create(self):
#         dummy_model = Menu.objects.create(name='Food1')
#         self.assertEqual(str(dummy_model.name), 'Food1')

class CategoryTest(TestCase):
    def test_category(self):
        category_test = Category.objects.create(name='Salad')
        category_test.save()
        self.assertEqual(str(category_test.name), 'Salad')


class MenuTest(TestCase):
    def setUp(self):
        self.first_menu = Menu.objects.create(
            category=Category.objects.create(name='Appetisers'),
            name='Menu1',
            description='Description',
            price=10,
            quantity=3
        )
        self.first_menu.save()

    def test_menu(self):
        self.assertEqual(str(self.first_menu.category), 'Appetisers')
        self.assertEqual(int(self.first_menu.price), 10)
