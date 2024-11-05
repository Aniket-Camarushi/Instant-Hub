from django.db import models

from UserServices.models import Users

# Create your models here.
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=False)
    image = models.TextField()
    description = models.TextField()
    display_order = models.IntegerField(default=0)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_categories')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.JSONField()
    description = models.TextField()
    specs = models.JSONField()
    html_content = models.TextField()
    highlights = models.JSONField()
    sku = models.CharField(max_length=255)
    initial_buying_price = models.FloatField()
    initial_selling_price = models.FloatField()
    weight = models.FloatField()
    dimensions = models.CharField(default='0x0x0', max_length=255)
    
    # Unit of Measurement
    uom = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    tax_percent = models.FloatField()
    brand = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE')
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    seo_keywords = models.JSONField()
    additional_details = models.JSONField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True, related_name='category_id_products')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_products')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class ProductReview(models.Model):
    id = models.AutoField(primary_key=True)
    review_images = models.JSONField()
    review = models.TextField()
    rating = models.FloatField()
    status = models.CharField(max_length=255, choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'),  ('REJECTED', 'REJECTED')], default='PENDING')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='product_id_products_review')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_products_review')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_products_review')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# End of code
