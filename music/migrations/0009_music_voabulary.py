# Generated by Django 4.2.6 on 2023-10-15 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_music_vocabs_alter_vocab_eng_alter_vocab_meaning'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='voabulary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
