# Generated by Django 4.1.6 on 2023-03-10 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='webapp.project'),
        ),
    ]