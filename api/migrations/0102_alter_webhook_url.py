# Generated by Django 3.2.8 on 2023-06-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0101_alter_country_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhook',
            name='url',
            field=models.CharField(help_text='Webhook URL address. If not empty, field indicates that task should be given not to a user in the system, but to a webhook. Only data from task directly preceding webhook is sent. All fields related to user assignment are ignored,if this field is not empty.', max_length=1000),
        ),
    ]
