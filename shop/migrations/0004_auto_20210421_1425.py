# Generated by Django 3.1.4 on 2021-04-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210421_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]