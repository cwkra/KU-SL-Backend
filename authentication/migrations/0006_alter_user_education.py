# Generated by Django 4.2.7 on 2024-03-07 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.OneToOneField(blank=True, db_column='education', null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.education'),
        ),
    ]
