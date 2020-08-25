# Generated by Django 3.1 on 2020-08-21 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_invitecode'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]