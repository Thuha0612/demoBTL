# Generated by Django 4.2.6 on 2023-10-15 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_vocab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]