from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True, choices=[('USA', 'USA')])
    profile_pic = models.TextField(blank=True, null=True)
    account_status = models.CharField(max_length=50, blank=True, null=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    role = models.CharField(max_length=50, blank=True, null=True, choices=[('Admin', 'Admin'), ('User', 'User'), ('Vendor', 'Vendor'), ('Customer', 'Customer'), ('Super Admin', 'Super Admin')])
    dob = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    social_media_links = models.JSONField(blank=True, null=True)
    additional_details = models.JSONField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True, choices=[('English', 'English')])
    department = models.CharField(max_length=50, blank=True, null=True, choices=[('IT', 'IT'),  ('HR', 'HR'), ('Finance', 'Finance'),  ('Marketing', 'Marketing'),  ('Sales', 'Sales'),  ('Operations', 'Operations'),   ('Logistics', 'Logistics'),  ('Customer Service', 'Customer Service'),   ('Production',  'Production'),  ('Quality Control', 'Quality Control'),   ('R&D', 'R&D'), ('Customer Service',  'Customer Service')])
    designation = models.CharField(max_length=50, blank=True, null=True, choices=[('Manager', 'Manager'), ('Team Lead', 'Team Lead'), ('Developer', 'Developer'), ('Designer', 'Designer'), ('Analyst', 'Analyst'), ('Intern', 'Intern'), ('Other', 'Other')])
    time_zone = models.CharField(max_length=50, blank=True, null=True, choices=[('UTC-05:00', 'UTC-05:00'), ('UTC-06:00', 'UTC-06:00'), ('UTC-07:00', 'UTC-07:00'), ('UTC-08:00', 'UTC-08:00'), ('UTC-09:00', 'UTC-09:00'), ('UTC-10:00', 'UTC-10:00'), ('UTC-04:00', 'UTC-04:00')])
    last_login = models.DateTimeField(blank=True,  null=True)
    last_device = models.CharField(max_length=50, blank=True, null=True)
    last_ip = models.GenericIPAddressField(blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True, choices=[('USD', 'USD')])
    domain_user_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_users')
    domain_name = models.CharField(max_length=50, blank=True, null=True)
    plan_type =  models.CharField(max_length=50, blank=True, null=True,  choices=[('Free', 'Free'), ('Paid', 'Paid')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def defaultkey():
        return 'username'
    
    def save(self, *args, **kwargs):
        if not self.domain_user_id and self.id:
            self.domain_user_id=self.domain_user_id
        super().save(*args, **kwargs)


class UserShippingAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_id_user_shipping_address')
    address_type = models.CharField(max_length= 50, blank=True, null=True, choices=[('Home', 'Home'), ('Work', 'Work'),  ('Other', 'Other')])
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=50, choices=[('USA', 'USA')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100)
    module_icon = models.CharField(null=True, blank=True, max_length=50)
    is_menu = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    module_url = models.CharField(null=True, blank=True, max_length=50)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parent_id_modules')
    display_order = models.IntegerField(default=0)
    module_description = models.CharField(null=True, blank=True, max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class UserPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_id_user_permissions')
    module = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name='module_id_user_permissions')
    is_view = models.BooleanField(default=False)
    is_add = models.BooleanField(default=False)
    is_edit = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    domain_user_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class ActivityLog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_id_activity_log')
    activity = models.TextField()
    activity_type = models.CharField(max_length=50, blank=True)
    activity_date = models.DateTimeField(auto_now_add=True)
    activity_ip = models.GenericIPAddressField()
    activity_device = models.CharField(max_length=50)
    domain_user_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# End of code
