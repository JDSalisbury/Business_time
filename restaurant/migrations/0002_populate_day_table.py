# Generated by Django 5.1 on 2024-08-18 15:34

from django.db import migrations


def populate_day_table(apps, schema_editor):
    Day = apps.get_model('restaurant', 'Day')

    initial_days = [
        {"name": "Monday", "abbr": "Mon", "is_weekend": False},
        {"name": "Tuesday", "abbr": "Tue", "is_weekend": False},
        {"name": "Wednesday", "abbr": "Wed", "is_weekend": False},
        {"name": "Thursday", "abbr": "Thu", "is_weekend": False},
        {"name": "Friday", "abbr": "Fri", "is_weekend": False},
        {"name": "Saturday", "abbr": "Sat", "is_weekend": True},
        {"name": "Sunday", "abbr": "Sun", "is_weekend": True},
    ]

    for day_data in initial_days:
        Day.objects.create(**day_data)


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_day_table),
    ]
