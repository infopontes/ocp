# Generated by Django 4.2.1 on 2023-06-25 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0008_localidades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mananciais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcda', models.CharField(max_length=6, verbose_name='GCDA')),
                ('capacidade', models.PositiveIntegerField(verbose_name='Capcidade')),
                ('latitude_decimal', models.CharField(max_length=20, verbose_name='Latitude')),
                ('longitude_decimal', models.CharField(max_length=20, verbose_name='Longitude')),
                ('status', models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo'), ('S', 'Suspenso')], default='I', max_length=1, verbose_name='Status')),
                ('municipio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.municipios', verbose_name='Município')),
            ],
            options={
                'verbose_name': 'Manancial',
                'verbose_name_plural': 'Mananciais',
                'ordering': ['gcda'],
            },
        ),
    ]