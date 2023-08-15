# Generated by Django 4.1.5 on 2023-02-06 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Api_grup_all', '0003_delete_fotos_alter_lista_options_and_more'),
        ('Infor_table_more', '0006_delete_fotos_delete_informacion_directa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('texto', models.TextField()),
                ('padre', models.CharField(choices=[('MenuButton', 'MenuButton'), ('Lista', 'Lista')], default='MenuButton', max_length=40)),
                ('activo', models.BooleanField(default=False)),
                ('PGRUPO', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api_grup_all.menubutton')),
                ('PGRUPO_Lista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api_grup_all.lista')),
            ],
            options={
                'verbose_name_plural': 'Informacion',
            },
        ),
        migrations.CreateModel(
            name='Tabla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_Info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Infor_table_more.informacion')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=40, null=True)),
                ('foto', models.ImageField(blank=True, upload_to='Galeria_Inform')),
                ('id_Info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Infor_table_more.informacion')),
            ],
        ),
        migrations.CreateModel(
            name='Campos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('id_tabla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Infor_table_more.tabla')),
            ],
        ),
    ]
