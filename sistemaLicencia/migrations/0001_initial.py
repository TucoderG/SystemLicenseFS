# Generated by Django 4.1 on 2022-10-14 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clave',
            fields=[
                ('clave', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaExamen', models.DateField()),
                ('tiempoLimite', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rendido', models.IntegerField()),
                ('aprobado', models.IntegerField()),
                ('reprobado', models.IntegerField()),
                ('ausente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('anteojos', models.BooleanField()),
                ('examenRendidos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('idPregunta', models.IntegerField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=150)),
                ('respuesta1', models.CharField(max_length=200)),
                ('respuesta2', models.CharField(max_length=200)),
                ('respuesta3', models.CharField(max_length=200)),
                ('respuesta4', models.CharField(max_length=200)),
                ('respuestaCorrecta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTurno', models.CharField(max_length=40)),
                ('fechaTurno', models.DateField()),
                ('idPersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaLicencia.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('idExamen', models.IntegerField(primary_key=True, serialize=False)),
                ('rendido', models.BooleanField(default=False, null=True)),
                ('preguntasCorrectas', models.IntegerField()),
                ('clave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaLicencia.clave')),
            ],
        ),
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('idPregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaLicencia.pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='clave',
            name='idPersona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaLicencia.persona'),
        ),
    ]
