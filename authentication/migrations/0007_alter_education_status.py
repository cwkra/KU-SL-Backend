# Generated by Django 4.2.7 on 2024-03-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='status',
            field=models.CharField(choices=[('ผู้กู้ยืมรายใหม่', 'ผู้กู้ยืมรายใหม่'), ('ผู้กู้ยืมรายเก่า', 'ผู้กู้ยืมรายเก่า')], default='ผู้กู้ยืมรายใหม่', max_length=150),
        ),
    ]
