# Generated by Django 2.1.4 on 2019-02-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190212_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category2',
            name='attr',
        ),
        migrations.AlterField(
            model_name='category1',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m', verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='category2',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m', verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='wastebook',
            name='account_date',
            field=models.DateTimeField(default='2019-02-12 22:31:44', verbose_name='记账日期'),
        ),
    ]
