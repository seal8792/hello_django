# Generated by Django 2.1.5 on 2019-02-18 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
