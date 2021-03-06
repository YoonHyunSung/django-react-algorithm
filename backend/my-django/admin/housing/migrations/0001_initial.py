# Generated by Django 3.2.5 on 2021-10-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('housing_median_age', models.FloatField()),
                ('total_rooms', models.FloatField()),
                ('tatal_bedrooms', models.FloatField()),
                ('population', models.FloatField()),
                ('households', models.FloatField()),
                ('median_income', models.FloatField()),
                ('median_house_value', models.FloatField()),
                ('ocean_prximity', models.TextField()),
            ],
            options={
                'db_table': 'housings',
            },
        ),
    ]
