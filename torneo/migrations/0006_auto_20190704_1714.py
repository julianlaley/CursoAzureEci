# Generated by Django 2.2.2 on 2019-07-04 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0005_fase_tipogrupos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fase',
            name='tipoGrupos',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='A', max_length=1, null=True),
        ),
    ]
