# Generated by Django 4.0.4 on 2022-07-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_alter_termspage_privacy_alter_termspage_privacy_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name': 'About page', 'verbose_name_plural': 'About page'},
        ),
        migrations.AlterModelOptions(
            name='contactspage',
            options={'verbose_name': 'Contacts page', 'verbose_name_plural': 'Contacts page'},
        ),
        migrations.AlterModelOptions(
            name='discountspage',
            options={'verbose_name': 'Discounts page', 'verbose_name_plural': 'Discounts page'},
        ),
        migrations.AlterModelOptions(
            name='refundpage',
            options={'verbose_name': 'Refund page', 'verbose_name_plural': 'Refund page'},
        ),
        migrations.AlterModelOptions(
            name='shippingpage',
            options={'verbose_name': 'Shipping page', 'verbose_name_plural': 'Shipping page'},
        ),
        migrations.AlterModelOptions(
            name='sizingpage',
            options={'verbose_name': 'Sizing page', 'verbose_name_plural': 'sizing page'},
        ),
        migrations.AlterModelOptions(
            name='termspage',
            options={'verbose_name': 'Terms page', 'verbose_name_plural': 'Terms page'},
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text_1',
            field=models.TextField(blank=True, default='', verbose_name='frst prt'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text_1_en',
            field=models.TextField(blank=True, default='', null=True, verbose_name='frst prt'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text_1_ru',
            field=models.TextField(blank=True, default='', null=True, verbose_name='frst prt'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text_1_uk',
            field=models.TextField(blank=True, default='', null=True, verbose_name='frst prt'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text_2',
            field=models.TextField(blank=True, default='', verbose_name='scnd prt'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text_2_en',
            field=models.TextField(blank=True, default='', null=True, verbose_name='scnd prt'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text_2_ru',
            field=models.TextField(blank=True, default='', null=True, verbose_name='scnd prt'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text_2_uk',
            field=models.TextField(blank=True, default='', null=True, verbose_name='scnd prt'),
        ),
    ]
