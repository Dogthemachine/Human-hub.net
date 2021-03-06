# Generated by Django 4.0.4 on 2022-07-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0007_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='media',
            field=models.CharField(default='https://catcult.club/media/', max_length=250, verbose_name='media url'),
        ),
        migrations.AddField(
            model_name='config',
            name='merchant_account',
            field=models.CharField(default='', max_length=64, verbose_name='merchant account'),
        ),
        migrations.AddField(
            model_name='config',
            name='merchant_domain_name',
            field=models.CharField(default='', max_length=64, verbose_name='merchant domain name'),
        ),
        migrations.AddField(
            model_name='config',
            name='merchant_secret',
            field=models.CharField(default='', max_length=128, verbose_name='merchant secret'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_en',
            field=models.CharField(default='грн', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_eur_en',
            field=models.CharField(default='Евр', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_eur_ru',
            field=models.CharField(default='Евр', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_eur_uk',
            field=models.CharField(default='Евр', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_ru',
            field=models.CharField(default='грн', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_uk',
            field=models.CharField(default='грн', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_usd_en',
            field=models.CharField(default='Долл', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_usd_ru',
            field=models.CharField(default='Долл', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='price_description_usd_uk',
            field=models.CharField(default='Долл', max_length=250, null=True, verbose_name='price_description'),
        ),
        migrations.AddField(
            model_name='config',
            name='service_url',
            field=models.CharField(default='', max_length=512, verbose_name='service URL'),
        ),
        migrations.AddField(
            model_name='config',
            name='static',
            field=models.CharField(default='https://catcult.club/static/', max_length=250, verbose_name='static url'),
        ),
        migrations.AlterField(
            model_name='config',
            name='price_description',
            field=models.CharField(default='грн', max_length=250, verbose_name='price_description'),
        ),
        migrations.AlterField(
            model_name='config',
            name='price_description_eur',
            field=models.CharField(default='Евр', max_length=250, verbose_name='price_description'),
        ),
        migrations.AlterField(
            model_name='config',
            name='price_description_usd',
            field=models.CharField(default='Долл', max_length=250, verbose_name='price_description'),
        ),
    ]
