from django.test import TestCase
from restaurant.models import Menu



class MenuItemTest(TestCase):
       def test_get_item(self):
	        item = Menu.objects.create(title='orange',price=2.3,inventory=3)
	        self.assertEqual(item.title,"orange")