# Generated by Django 4.1.6 on 2023-02-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deleted_at',
            field=models.DateField(default=None, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='task',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='удалено'),
        ),
    ]
