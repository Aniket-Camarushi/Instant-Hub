# Generated by Django 4.2.16 on 2024-10-25 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('InventoryServices', '0001_initial'),
        ('ProductServices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OrderServices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_warehouse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_warehouse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='warehouse_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_manager_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rackandshelvesandfloor',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_rack_shelf_floor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rackandshelvesandfloor',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_rack_shelf_floor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rackandshelvesandfloor',
            name='warehouse_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_id_rack_shelf_floor', to='InventoryServices.warehouse'),
        ),
        migrations.AddField(
            model_name='inventorylog',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_inventory_log', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventorylog',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_inventory_log', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventorylog',
            name='inventory_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_id_inventory_log', to='InventoryServices.inventory'),
        ),
        migrations.AddField(
            model_name='inventorylog',
            name='purchase_order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_id_inventory_log', to='OrderServices.purchaseorder'),
        ),
        migrations.AddField(
            model_name='inventorylog',
            name='rack_shelf_floor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rack_shelf_floor_id_inventory_log', to='InventoryServices.rackandshelvesandfloor'),
        ),
        migrations.AddField(
            model_name='inventorylog',
            name='sales_order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_order_id_inventory_log', to='OrderServices.salesorder'),
        ),
        migrations.AddField(
            model_name='inventorylog',
            name='warehouse_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_id_inventory_log', to='InventoryServices.warehouse'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_inventory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventory',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_inventory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_id_inventory', to='ProductServices.products'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='purchase_order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_id_inventory', to='OrderServices.purchaseorder'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='purchase_order_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_item_id_inventory', to='OrderServices.purchaseorderitems'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='purchase_order_item_inwarded_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_item_inwarded_item_id_inventory', to='OrderServices.purchaseorderiteminwardedlog'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='rack_shelf_floor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rack_shelf_floor_id_inventory', to='InventoryServices.rackandshelvesandfloor'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='warehouse_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_id_inventory', to='InventoryServices.warehouse'),
        ),
    ]
