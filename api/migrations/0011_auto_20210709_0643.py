# Generated by Django 3.2.5 on 2021-07-09 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210709_0628'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ranklimit',
            unique_together={('rank', 'stage')},
        ),
        migrations.AlterUniqueTogether(
            name='rankrecord',
            unique_together={('user', 'rank')},
        ),
    ]