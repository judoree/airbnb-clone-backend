# Generated by Django 5.0.3 on 2024-03-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_house_pet_allowed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='pet_allowed',
        ),
        migrations.AddField(
            model_name='house',
            name='pets_allowed',
            field=models.BooleanField(default=True, help_text='Does this house allow pets?', verbose_name='Pets Allowed?'),
        ),
        migrations.AlterField(
            model_name='house',
            name='price_per_night',
            field=models.PositiveIntegerField(help_text='Positive Numbers Only', verbose_name='Price'),
        ),
    ]
