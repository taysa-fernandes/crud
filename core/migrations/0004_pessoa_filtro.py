# Generated by Django 3.2.19 on 2023-05-16 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230516_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='filtro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.filtro'),
        ),
    ]
