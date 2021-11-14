# Generated by Django 3.2.9 on 2021-11-13 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('copytter', '0002_auto_20211114_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_user_id',
            field=models.CharField(default='nwzvcbta5m', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('machine', 'BOT'), ('block', '凍結'), ('close', '非公開'), ('official', '公式'), ('public', '一般')], default='publish', max_length=10),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=8)),
                ('media_url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]