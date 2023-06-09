# Generated by Django 4.2.1 on 2023-06-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_cookerphoto_dishwasherphoto_dryphoto_microwavephoto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv',
            name='outputs',
            field=models.CharField(max_length=255, verbose_name='Выходы для переферии'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=255)),
                ('items', models.ManyToManyField(to='catalog.item', verbose_name='Содержимое')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]
