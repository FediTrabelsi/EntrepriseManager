# Generated by Django 2.2.6 on 2019-11-10 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offres', '0002_auto_20191110_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='Entreprise',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Entreprises.Entreprise'),
        ),
    ]
