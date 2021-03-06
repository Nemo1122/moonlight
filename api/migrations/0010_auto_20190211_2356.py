# Generated by Django 2.1.4 on 2019-02-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190211_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category1',
            name='icon_height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category1',
            name='icon_width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category2',
            name='icon_height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category2',
            name='icon_width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon_height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon_width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wastebook',
            name='account_date',
            field=models.DateTimeField(default='2019-02-11 23:56:02', verbose_name='记账日期'),
        ),
    ]
