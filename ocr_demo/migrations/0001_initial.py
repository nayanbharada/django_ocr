# Generated by Django 4.1.6 on 2023-02-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=50)),
                ('category_one', models.FloatField()),
                ('category_two', models.FloatField()),
                ('category_three', models.FloatField()),
                ('category_four', models.FloatField()),
            ],
        ),
    ]
