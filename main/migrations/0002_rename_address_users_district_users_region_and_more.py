# Generated by Django 5.0.2 on 2024-02-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='address',
            new_name='district',
        ),
        migrations.AddField(
            model_name='users',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
