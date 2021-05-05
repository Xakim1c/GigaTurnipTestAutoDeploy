# Generated by Django 3.2.1 on 2021-05-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210505_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='out_stages',
        ),
        migrations.AddField(
            model_name='stage',
            name='in_stages',
            field=models.ManyToManyField(blank=True, related_name='out_stages', to='api.Stage'),
        ),
    ]
