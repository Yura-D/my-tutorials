# Generated by Django 2.2.12 on 2020-04-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_tutorial_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
