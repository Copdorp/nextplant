# Generated by Django 3.2.5 on 2021-08-28 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210827_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='api.owner'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='api.owner'),
        ),
    ]
