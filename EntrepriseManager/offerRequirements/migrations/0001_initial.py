# Generated by Django 2.2.7 on 2019-11-16 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offres', '0003_auto_20191110_1230'),
        ('skills', '0002_auto_20191115_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='offres.Offer')),
                ('skill', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='skills.skill')),
            ],
        ),
    ]
