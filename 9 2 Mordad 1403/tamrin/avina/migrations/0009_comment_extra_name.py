# Generated by Django 5.0.4 on 2024-07-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avina', '0008_alter_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='extra_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
