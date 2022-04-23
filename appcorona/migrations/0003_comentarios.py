# Generated by Django 4.0.1 on 2022-03-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcorona', '0002_alter_empleo_empleos_disponibles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('comentario', models.TextField()),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
