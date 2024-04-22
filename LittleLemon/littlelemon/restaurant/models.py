from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    noofguests = models.SmallIntegerField(default=1)
	
    def __str__(self):
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory = models.SmallIntegerField()
   def __str__(self):
        return self.title+":"+str(self.price)



