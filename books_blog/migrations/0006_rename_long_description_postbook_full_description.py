# Generated by Django 4.1.2 on 2022-10-21 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_blog', '0005_rename_description_postbook_short_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postbook',
            old_name='long_description',
            new_name='full_description',
        ),
    ]
