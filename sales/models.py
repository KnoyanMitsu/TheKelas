from django.db import models

# Create your models here.
class ProductCategory(models.Model):
	name = models.CharField(max_length=250, unique=True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

class Product(models.Model):
	"""docstring for Product"""
	name = models.CharField(max_length=250, unique=True)
	product_category = models.ForeignKey(
		ProductCategory,
		related_name = 'products',
		on_delete = models.CASCADE
		)
	production_date = models.DateTimeField()
	price = models.IntegerField()
	owner = models.ForeignKey(
		'auth.User',
		related_name= 'products',
		on_delete= models.CASCADE
	)	

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name


class Receipt(models.Model):
	receipt_date = models.DateTimeField()
	no_resi = models.CharField(max_length=250, unique=True)
	total = models.IntegerField()
	class Meta:
		ordering = ('no_resi',)

	def __str__(self):
		return self.no_resi

class Sales(models.Model):
	product = models.ForeignKey(
		Product,
		related_name = 'sales',
		on_delete = models.CASCADE
		)
	receipt = models.ForeignKey(
		Receipt,
		related_name = 'sales',
		on_delete = models.CASCADE
		)
	quantity = models.IntegerField()
	sub_total = models.IntegerField()

	class Meta:
		ordering = ('receipt',)