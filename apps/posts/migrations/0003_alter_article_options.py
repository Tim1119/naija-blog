# Generated by Django 4.1.4 on 2022-12-17 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on'], 'verbose_name': 'Article', 'verbose_name_plural': 'Article'},
        ),
    ]