# Generated by Django 4.1.7 on 2023-03-06 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rembanapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.FloatField()),
                ('NumCuenta', models.CharField(max_length=50)),
                ('Beneficiario', models.CharField(max_length=100)),
                ('Concepto', models.TextField(max_length=200)),
                ('Banco', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rembanapp.usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Ordenes',
        ),
    ]
