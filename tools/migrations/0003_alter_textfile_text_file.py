# Generated by Django 4.0.5 on 2022-08-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_alter_textfile_text_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='Text_file',
            field=models.FileField(upload_to=''),
        ),
    ]