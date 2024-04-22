from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def test_getall(self):
	     item1 = Menu.objects.create(title='orange',price=2.3,inventory=8)
	     item2 = Menu.objects.create(title='carrot',price=5.3,inventory=8)
	     self.assertEqual(item1.title,"orange")
	     self.assertEqual(item2.title,"carrot")