# Generated by Django 5.1.1 on 2024-09-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('family', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(default='Bon', max_length=50)),
            ],
        ),
    ]
