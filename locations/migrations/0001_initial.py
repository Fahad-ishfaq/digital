# Generated by Django 4.0 on 2021-12-30 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('main', models.CharField(max_length=30, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=10)),
                ('surface_area', models.IntegerField(verbose_name='Surface Area of the country in km')),
                ('population', models.IntegerField(verbose_name='Population')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
