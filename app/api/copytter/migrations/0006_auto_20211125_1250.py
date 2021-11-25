# Generated by Django 3.2.9 on 2021-11-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copytter', '0005_auto_20211125_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='relation_id',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_user_id',
            field=models.CharField(default='STMzHDpWXj', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('public', '一般'), ('official', '公式'), ('machine', 'BOT'), ('block', '凍結'), ('close', '非公開')], default='publish', max_length=10),
        ),
    ]
