# Generated by Django 2.1.5 on 2019-02-16 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_auto_20190214_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
