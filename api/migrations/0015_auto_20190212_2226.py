# Generated by Django 2.1.4 on 2019-02-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190212_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastebook',
            name='account_date',
            field=models.DateTimeField(default='2019-02-12 22:26:52', verbose_name='记账日期'),
        ),
    ]
