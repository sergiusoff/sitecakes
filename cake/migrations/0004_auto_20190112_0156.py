# Generated by Django 2.1.4 on 2019-01-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_auto_20190112_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
