# Generated by Django 4.2.7 on 2024-03-19 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_alter_notification_receiver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.CharField(default='แจ้งผล', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
