# Generated by Django 3.2.6 on 2021-08-03 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_case_chain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='default_track',
            field=models.ForeignKey(blank=True, help_text='Default track id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_campaigns', to='api.track'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.TextField(blank=True, help_text='Instance description'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(help_text='Instance name', max_length=100),
        ),
        migrations.AlterField(
            model_name='chain',
            name='campaign',
            field=models.ForeignKey(help_text='Campaign id', on_delete=django.db.models.deletion.CASCADE, related_name='chains', to='api.campaign'),
        ),
        migrations.AlterField(
            model_name='chain',
            name='description',
            field=models.TextField(blank=True, help_text='Instance description'),
        ),
        migrations.AlterField(
            model_name='chain',
            name='name',
            field=models.CharField(help_text='Instance name', max_length=100),
        ),
        migrations.AlterField(
            model_name='conditionalstage',
            name='conditions',
            field=models.JSONField(help_text='JSON logic conditions', null=True),
        ),
        migrations.AlterField(
            model_name='conditionalstage',
            name='pingpong',
            field=models.BooleanField(default=False, help_text="If True, makes 'in stages' task incomplete"),
        ),
        migrations.AlterField(
            model_name='rank',
            name='description',
            field=models.TextField(blank=True, help_text='Instance description'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='name',
            field=models.CharField(help_text='Instance name', max_length=100),
        ),
        migrations.AlterField(
            model_name='rank',
            name='stages',
            field=models.ManyToManyField(help_text='Stages id', related_name='ranks', through='api.RankLimit', to='api.TaskStage'),
        ),
        migrations.AlterField(
            model_name='ranklimit',
            name='is_creation_open',
            field=models.BooleanField(default=True, help_text='Allow user to create a task'),
        ),
        migrations.AlterField(
            model_name='ranklimit',
            name='is_listing_allowed',
            field=models.BooleanField(default=False, help_text='Allow user to see the list of created tasks'),
        ),
        migrations.AlterField(
            model_name='ranklimit',
            name='is_selection_open',
            field=models.BooleanField(default=True, help_text='Allow user to select a task'),
        ),
        migrations.AlterField(
            model_name='ranklimit',
            name='is_submission_open',
            field=models.BooleanField(default=True, help_text='Allow user to submit a task'),
        ),
        migrations.AlterField(
            model_name='ranklimit',
            name='open_limit',
            field=models.IntegerField(default=0, help_text='The maximum number of tasks that can be opened at the same time for a user'),
        ),
        migrations.AlterField(
            model_name='ranklimit',
            name='rank',
            field=models.ForeignKey(help_text='Rank id', on_delete=django.db.models.deletion.CASCADE, to='api.rank'),
        ),
        migrations.AlterField(
            model_name='ranklimit',
            name='stage',
            field=models.ForeignKey(help_text='Stage id', on_delete=django.db.models.deletion.CASCADE, related_name='ranklimits', to='api.taskstage'),
        ),
        migrations.AlterField(
            model_name='ranklimit',
            name='total_limit',
            field=models.IntegerField(default=0, help_text='The maximum number of tasks that user can obtain'),
        ),
        migrations.AlterField(
            model_name='rankrecord',
            name='rank',
            field=models.ForeignKey(help_text='Rank id', on_delete=django.db.models.deletion.CASCADE, to='api.rank'),
        ),
        migrations.AlterField(
            model_name='rankrecord',
            name='user',
            field=models.ForeignKey(help_text='User id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stage',
            name='chain',
            field=models.ForeignKey(help_text='Chain id', on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='api.chain'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='description',
            field=models.TextField(blank=True, help_text='Instance description'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='in_stages',
            field=models.ManyToManyField(blank=True, help_text='List of previous id stages', related_name='out_stages', to='api.Stage'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='name',
            field=models.CharField(help_text='Instance name', max_length=100),
        ),
        migrations.AlterField(
            model_name='stage',
            name='x_pos',
            field=models.DecimalField(decimal_places=14, help_text="Starting position of 'x' coordinate to draw on Giga Turnip Chain frontend interface", max_digits=17),
        ),
        migrations.AlterField(
            model_name='stage',
            name='y_pos',
            field=models.DecimalField(decimal_places=14, help_text="Starting position of 'y' coordinate to draw on Giga Turnip Chain frontend interface", max_digits=17),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, help_text='User id who is responsible for the task', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='case',
            field=models.ForeignKey(blank=True, help_text='Case id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.case'),
        ),
        migrations.AlterField(
            model_name='task',
            name='in_tasks',
            field=models.ManyToManyField(blank=True, help_text='Preceded tasks', related_name='out_tasks', to='api.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='responses',
            field=models.JSONField(blank=True, help_text='User generated responses (answers)', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='stage',
            field=models.ForeignKey(help_text='Stage id', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.taskstage'),
        ),
        migrations.AlterField(
            model_name='taskstage',
            name='allow_multiple_files',
            field=models.BooleanField(default=False, help_text='Allow user to upload multiple files'),
        ),
        migrations.AlterField(
            model_name='taskstage',
            name='assign_user_by',
            field=models.CharField(choices=[('RA', 'Rank'), ('ST', 'Stage')], default='RA', help_text="User assignment method (by 'Stage' or by 'Rank')", max_length=2),
        ),
        migrations.AlterField(
            model_name='taskstage',
            name='assign_user_from_stage',
            field=models.ForeignKey(blank=True, help_text='Stage id. User from assign_user_from_stage will be assigned to a task', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_user_to_stages', to='api.stage'),
        ),
        migrations.AlterField(
            model_name='taskstage',
            name='displayed_prev_stages',
            field=models.ManyToManyField(blank=True, help_text='List of previous stages (tasks data) to be shown in current stage', related_name='displayed_following_stages', to='api.Stage'),
        ),
        migrations.AlterField(
            model_name='taskstage',
            name='is_creatable',
            field=models.BooleanField(default=False, help_text='Allow user to create a task manually'),
        ),
        migrations.AlterField(
            model_name='taskstage',
            name='json_schema',
            field=models.TextField(blank=True, help_text='Defines the underlying data to be shown in the UI (objects, properties, and their types)', null=True),
        ),
        migrations.AlterField(
            model_name='taskstage',
            name='library',
            field=models.CharField(blank=True, help_text='Type of JSON form library', max_length=200),
        ),
        migrations.AlterField(
            model_name='taskstage',
            name='ui_schema',
            field=models.TextField(blank=True, help_text='Defines how JSON data is rendered as a form, e.g. the order of controls, their visibility, and the layout', null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='campaign',
            field=models.ForeignKey(help_text='Campaign id', on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='api.campaign'),
        ),
        migrations.AlterField(
            model_name='track',
            name='default_rank',
            field=models.ForeignKey(blank=True, help_text='Rank id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.rank'),
        ),
        migrations.AlterField(
            model_name='track',
            name='description',
            field=models.TextField(blank=True, help_text='Instance description'),
        ),
        migrations.AlterField(
            model_name='track',
            name='name',
            field=models.CharField(help_text='Instance name', max_length=100),
        ),
        migrations.AlterField(
            model_name='track',
            name='ranks',
            field=models.ManyToManyField(help_text='Ranks id', related_name='ranks', to='api.Rank'),
        ),
        migrations.AlterField(
            model_name='webhookstage',
            name='json_schema',
            field=models.TextField(blank=True, help_text='Defines the underlying data to be shown in the UI (objects, properties, and their types)', null=True),
        ),
        migrations.AlterField(
            model_name='webhookstage',
            name='library',
            field=models.CharField(blank=True, help_text='Type of JSON form library', max_length=200),
        ),
        migrations.AlterField(
            model_name='webhookstage',
            name='ui_schema',
            field=models.TextField(blank=True, help_text='Defines how JSON data is rendered as a form, e.g. the order of controls, their visibility, and the layout', null=True),
        ),
    ]