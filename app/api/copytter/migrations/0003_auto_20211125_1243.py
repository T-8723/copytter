# Generated by Django 3.2.9 on 2021-11-25 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copytter', '0002_entry_follow_media_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copytter.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_user_id',
            field=models.CharField(default='WrkeT0LjLd', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('public', '一般'), ('block', '凍結'), ('official', '公式'), ('machine', 'BOT'), ('close', '非公開')], default='publish', max_length=10),
        ),
    ]