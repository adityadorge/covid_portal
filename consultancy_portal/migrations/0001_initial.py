# Generated by Django 3.2.9 on 2022-04-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30)),
                ('cases', models.IntegerField()),
                ('todaysCases', models.IntegerField()),
                ('death', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('active', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
    ]
