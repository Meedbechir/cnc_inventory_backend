# Generated by Django 5.1.1 on 2024-09-30 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cnc_app', '0002_rename_location_article_emplacement_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='quantité',
            new_name='quantite',
        ),
    ]
