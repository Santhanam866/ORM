# Generated by Django 5.1.2 on 2024-10-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('Accountno', models.IntegerField(primary_key='Accountno', serialize=False)),
                ('Aadharno', models.IntegerField()),
                ('DoB', models.DateField()),
                ('Email', models.EmailField(default='example@gmail.com', max_length=254)),
                ('Branch', models.CharField(max_length=21)),
            ],
        ),
    ]
