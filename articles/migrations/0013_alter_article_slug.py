# Generated by Django 3.2.18 on 2023-10-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default='_', editable=False, unique=True),
        ),
    ]
