# Generated by Django 2.1.1 on 2018-09-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_auto_20180927_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Принят в обработку', 'Принят в обработку'), ('Выполняется', 'Выполняется'), ('Оплачен', 'Оплачен')], max_length=100),
        ),
    ]