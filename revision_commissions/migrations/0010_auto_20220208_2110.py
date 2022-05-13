# Generated by Django 3.2.9 on 2022-02-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision_commissions', '0009_auto_20220208_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization_gu',
            name='type',
            field=models.CharField(default='ГУ', max_length=5, verbose_name='Тип организации'),
        ),
        migrations.AddField(
            model_name='organization_kvazi',
            name='type',
            field=models.CharField(default='КВАЗИ', max_length=5, verbose_name='Тип организации'),
        ),
    ]