# Generated by Django 4.2.5 on 2023-09-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_order_customer_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_mod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=200)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
