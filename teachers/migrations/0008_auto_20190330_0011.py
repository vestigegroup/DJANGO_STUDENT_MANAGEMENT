# Generated by Django 2.1.7 on 2019-03-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_auto_20190330_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='techer_id',
            field=models.CharField(max_length=6, null=True, unique=True),
        ),
    ]