# Generated by Django 4.1.1 on 2022-11-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0003_alter_invoice_line_one_total_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]