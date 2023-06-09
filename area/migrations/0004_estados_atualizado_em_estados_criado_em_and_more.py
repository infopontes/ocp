# Generated by Django 4.2.1 on 2023-06-12 00:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0003_alter_municipios_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='estados',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AddField(
            model_name='estados',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='municipios',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AddField(
            model_name='municipios',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='municipios',
            name='estado_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='area.estados', verbose_name='Estados'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estados',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='estados',
            name='uf',
            field=models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='UF'),
        ),
    ]
