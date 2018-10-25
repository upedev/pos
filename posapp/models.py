from django.db import models
from django.utils import timezone


class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True, default="some@email.com")
    password = models.CharField(max_length=500, blank=False, default="pass123")
    user_created_at = models.DateField(default=timezone.now)
    user_updated_at = models.DateField(auto_now=True)
    user_isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class restaurent(models.Model): # stores all the restaurents.
	rest_id = models.AutoField(primary_key=True)						# pk
	rest_name = models.CharField(max_length=30)
	is_active = models.BooleanField(default=True)

class branch(models.Model): # branches for the restaurent.
	branch_id = models.AutoField(primary_key=True)						# pk
	branch_name = models.CharField(max_length=30)
	#rest_id 	# fk
	branch_address = models.TextField();

class item(models.Model): # items in the branch of restaurent.
	item_id = models.AutoField(primary_key=True)						# pk
	item_name = models.CharField(max_length=30)
	item_desc = models.TextField()
	#category_id		# fk
	item_price = models.DecimalField(max_digits=3, decimal_places=2)
	#rest_id		# fk
	is_veg = models.BooleanField()
	
class category(models.Model): # category for the items.
	category_id = models.AutoField(primary_key=True)					# pk
	cat_desc = models.TextField()
	cat_name = models.CharField(max_length=20)

class order(models.Model): # stores the orders.
	order_id = models.AutoField(primary_key=True)						# pk
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	#discount_id
	created_at = models.DateTimeField(default=timezone.now)
	payment_mode = models.CharField(max_length=10)

class order_desc(models.Model): # items in the order.
	order_id = models.AutoField(primary_key=True)						# pk
	#item_id
	quantity = models.IntegerField()
	#total_price
	
class discount(models.Model): # type and discount value.
	discount_id = models.AutoField(primary_key=True)					# pk
	#discount_type
	discount = models.IntegerField()
	#rest_id
