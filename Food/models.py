from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField("Item Name",max_length=200)
    item_desc = models.CharField("Item Discription",max_length=200)
    item_price = models.IntegerField("Item Price")
    item_image = models.CharField("Item Image",max_length=200,default="https://image.flaticon.com/icons/svg/1344/1344788.svg")


    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("Food:details",kwargs = {"pk":self.pk})