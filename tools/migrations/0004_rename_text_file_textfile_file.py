# Generated by Django 4.0.5 on 2022-08-17 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_alter_textfile_text_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textfile',
            old_name='Text_file',
            new_name='File',
        ),
    ]