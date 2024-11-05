from django.db import models

from UserServices.models import Users
from ProductServices.models import Products
from OrderServices.models import PurchaseOrder, PurchaseOrderItems, PurchaseOrderItemInwardedLog
from OrderServices.models import SalesOrder, SalesOrderItems, SalesOrderItemOutwardedLog

# Create your models here.

class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=255, blank=False, null=False)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    warehouse_manager = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='warehouse_manager_id')
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    status = models.CharField(max_length=255, choices=[('Active',  'Active'), ('Inactive', 'Inactive')])
    size = models.CharField(max_length=255, choices=[('Small',  'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    capacity = models.CharField(max_length=255,  choices=[('Low',  'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low')
    warehouse_type = models.CharField(max_length=255, choices=[('Owned',   'Owned'), ('Rented', 'Rented')], default='Owned')
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_warehouse')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_warehouse')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RackAndShelvesAndFloor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='warehouse_id_rack_shelf_floor')
    rack = models.CharField(max_length=255, blank=False, null=False)
    shelf = models.CharField(max_length=255, blank=False, null=False)
    floor = models.CharField(max_length=255, blank=False, null=False)
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_rack_shelf_floor')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_rack_shelf_floor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """
    rack_number = models.CharField(max_length=255)
    rack_size = models.CharField(max_length=255, choices=[('Small',  'Small'),
                                                          ('Medium', 'Medium'),
                                                          ('Large', 'Large')])
    rack_type = models.CharField(max_length=255, choices=[('Fixed',   'Fixed'),  ('Adjustable', 'Adjustable')]) 
    rack_status = models.CharField(max_length=255, choices=[('Active',  'Active'),
                                                            ('Inactive', 'Inactive')])
    """


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, blank=True, null=True, related_name='purchase_order_id_inventory')
    purchase_order_item_id = models.ForeignKey(PurchaseOrderItems, on_delete=models.CASCADE, blank=True, null=True, related_name='purchase_order_item_id_inventory')
    purchase_order_item_inwarded_item_id = models.ForeignKey(PurchaseOrderItemInwardedLog, on_delete=models.CASCADE, blank=True, null=True, related_name='purchase_order_item_inwarded_item_id_inventory')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True, related_name='product_id_inventory')
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True, related_name='warehouse_id_inventory')
    rack_shelf_floor_id = models.ForeignKey(RackAndShelvesAndFloor, on_delete=models.CASCADE, blank=True, null=True, related_name='rack_shelf_floor_id_inventory')
    quantity = models.IntegerField()
    mrp = models.CharField(max_length=255, blank=True, null=True)
    batch_number = models.CharField(max_length=255, blank=True, null=True)
    discount_type = models.CharField(max_length=255, blank=True, null=True, choices=[('Amount','Amount'),('Percentage','Percentage')],  default='Percentage')
    discount_amount = models.FloatField()
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    manufacturing_date = models.DateTimeField(blank=True, null=True)
    unit_of_measurement = models.CharField(max_length=255)
    ptr = models.CharField(max_length=255, blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    quantity_inwarded = models.IntegerField()
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_status = models.CharField(max_length=255, choices=[('In_Stock','In_Stock'),('Out_Of_Stock','Out_Of_Stock')],default='In_Stock', blank=True, null=True)
    inward_type  = models.CharField(max_length=255, choices=[('Purchase','Purchase'),('Return','Return'), ('Replacement',  'Replacement'),  ('Warehouse Transfer', 'Warehouse Transfer')],  default='Purchase', blank=True, null=True)
    additional_details  = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_inventory')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_inventory')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class  InventoryLog(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, blank=True, null=True, related_name='purchase_order_id_inventory_log')
    sales_order_id = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_order_id_inventory_log')
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=True, null=True,  related_name='inventory_id_inventory_log')
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True, related_name='warehouse_id_inventory_log')
    rack_shelf_floor_id = models.ForeignKey(RackAndShelvesAndFloor, on_delete=models.CASCADE, blank=True, null=True, related_name='rack_shelf_floor_id_inventory_log')
    quantity = models.IntegerField()
    status = models.CharField(max_length=255, choices=[('Inward','Inward'),('Outward','Outward'), ('Damaged', 'Damaged'), ('Lost', 'Lost'), ('Expired', 'Expired'), ('Returned', 'Returned'), ('Adjustment', 'Adjustment'), ('Warehouse Transfer', 'Warehouse Transfer')], default='In_Stock', blank =True, null=True)
    additional_details  = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True , related_name='domain_user_id_inventory_log')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank =True, related_name='added_by_user_id_inventory_log')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# End of code
