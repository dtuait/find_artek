# Generated by Django 4.1.4 on 2023-03-02 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_delete_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='modified_date',
        ),
    ]