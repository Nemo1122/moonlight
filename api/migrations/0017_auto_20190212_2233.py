# Generated by Django 2.1.4 on 2019-02-12 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190212_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastebook',
            name='account_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='记账日期'),
        ),
    ]
