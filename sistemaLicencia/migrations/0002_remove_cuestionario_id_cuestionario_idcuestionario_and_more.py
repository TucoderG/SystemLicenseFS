# Generated by Django 4.1 on 2022-10-14 22:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaLicencia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuestionario',
            name='id',
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='idCuestionario',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examen',
            name='idcuest',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sistemaLicencia.cuestionario'),
            preserve_default=False,
        ),
    ]
