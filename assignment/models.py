from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = 'product'
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=55, null=True)
    def __str__(self):
        return self.product_id

class Sales(models.Model):
    class Meta:
        db_table = 'sales'
    sales_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    year = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.sales_id