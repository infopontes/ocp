# Generated by Django 4.2.1 on 2023-06-25 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0006_remove_municipios_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=7)),
                ('municipio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.municipios', verbose_name='Município')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
                'ordering': ['nome'],
            },
        ),
    ]
