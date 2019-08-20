# Generated by Django 2.2.4 on 2019-08-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_customer_time_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, '普通'), (2, '批发'), (3, 'VIP')], default=1),
        ),
    ]
