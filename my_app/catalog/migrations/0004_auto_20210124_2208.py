# Generated by Django 3.1.5 on 2021-01-24 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210124_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('test_permission', 'Test permission'))},
        ),
    ]
