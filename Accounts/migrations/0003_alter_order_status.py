# Generated by Django 5.1.5 on 2025-02-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_tag_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delevered', 'Delivered')], max_length=255),
        ),
    ]
