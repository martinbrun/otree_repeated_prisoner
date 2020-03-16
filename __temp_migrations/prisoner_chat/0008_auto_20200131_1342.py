# Generated by Django 2.2.4 on 2020-01-31 12:42

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner_chat', '0007_auto_20200131_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='chat_end_time',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='chat_start_time',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
    ]
