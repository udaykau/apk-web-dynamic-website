from django.db import models
import os


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


def uploads(instance, filename):
    os.path.join('media/apkshopee/', instance.Product_Name)
    dire = '{0}/{1}'.format(instance.Product_Name, filename)
    return str(dire)


class Product(models.Model):
    sno = models.AutoField(primary_key=True)
    Active = models.BooleanField(default=True)
    Total_Stock = models.IntegerField(default=0)
    Availability = models.CharField(max_length=100, default='In Stock')
    Image1 = models.ImageField(null=True, blank=True, upload_to=uploads)
    Image2 = models.ImageField(null=True, blank=True, upload_to=uploads)
    Image3 = models.ImageField(null=True, blank=True, upload_to=uploads)
    Image4 = models.ImageField(null=True, blank=True, upload_to=uploads)
    Original_Price = models.CharField(max_length=300, default='0')
    Discount_Price = models.CharField(max_length=300, default='0')
    Product_Name = models.CharField(max_length=300)
    gender = (
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids')
    )
    Gender = models.CharField(max_length=100, choices=gender, null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Short_Description = models.TextField(max_length=3000)
    Long_Description = models.TextField(max_length=50000)
    Minimum_Quantity = models.IntegerField(default=1)
    Size = models.BooleanField(default=False)
    Size_Description = models.TextField(max_length=400, null=True, blank=True)
    Color = models.BooleanField(default=False)
    Color_Description = models.TextField(max_length=400, null=True, blank=True)
    Fabric = models.BooleanField(default=False)
    Fabric_Description = models.TextField(max_length=400, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class cart(models.Model):
    sno = models.AutoField(primary_key=True)
    Image = models.ImageField(null=True, blank=True, upload_to='media/Cart/')
    Merchant_Email = models.CharField(max_length=100)
    Product_Sno = models.CharField(max_length=20)
    Product_Name = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Total_Price = models.CharField(max_length=100, null=True, blank=True)
    Qty = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)


class Total_Cart(models.Model):
    sno = models.AutoField(primary_key=True)
    Merchant_Email = models.CharField(max_length=100)
    Total_Item = models.CharField(max_length=100)
    Total_Price = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)


class Billing_Address(models.Model):
    sno = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=300, default='-')
    Product_Sno = models.CharField(max_length=2000)
    Product_Name = models.CharField(max_length=2000)
    Prices = models.CharField(max_length=2000, null=True, blank=True)
    Total_Price = models.CharField(max_length=2000)
    Qty = models.CharField(max_length=100)
    Merchant_mail = models.CharField(max_length=500)
    Phone = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
