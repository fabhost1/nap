# Generated by Django 3.2.12 on 2022-03-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coffeshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('address', models.TextField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('url', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'coffeshop',
            },
        ),
        migrations.CreateModel(
            name='medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('address', models.TextField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('url', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'medical',
            },
        ),
        migrations.CreateModel(
            name='shoppingmall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('address', models.TextField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('url', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'shoppingmall',
            },
        ),
    ]
