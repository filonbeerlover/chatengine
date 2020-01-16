# Generated by Django 3.0.2 on 2020-01-16 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('themes', '0002_auto_20200113_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='author',
            field=models.ForeignKey(limit_choices_to={'profile__is_teacher': True}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
