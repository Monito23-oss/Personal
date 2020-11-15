# Generated by Django 3.1.1 on 2020-10-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mi Depertamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]
