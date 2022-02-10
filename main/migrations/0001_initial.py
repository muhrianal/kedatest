# Generated by Django 3.2.12 on 2022-02-09 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_code', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('material_name', models.CharField(max_length=300)),
                ('material_buy_price', models.IntegerField()),
                ('material_type', models.CharField(choices=[('Fabric', 'Fabric'), ('Jeans', 'Jeans'), ('Cotton', 'Cotton')], max_length=50)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
    ]