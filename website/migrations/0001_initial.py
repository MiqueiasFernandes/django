# Generated by Django 2.2.15 on 2020-09-04 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneOntology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('go_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('go_type', models.PositiveIntegerField(choices=[(0, 'CC'), (1, 'BP'), (2, 'MF')])),
            ],
        ),
        migrations.CreateModel(
            name='Pfam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfam_id', models.CharField(max_length=7, unique=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxonomy_id', models.PositiveIntegerField(unique=True)),
                ('organism_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UniprotKb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession', models.CharField(max_length=12, unique=True)),
                ('sequence', models.TextField()),
                ('lenght', models.PositiveIntegerField(blank=True, null=True)),
                ('gos', models.ManyToManyField(to='website.GeneOntology')),
                ('pfam', models.ManyToManyField(to='website.Pfam')),
                ('taxonomy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Taxonomy')),
            ],
        ),
        migrations.CreateModel(
            name='PDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession', models.CharField(max_length=4, unique=True)),
                ('resolution', models.FloatField()),
                ('method', models.PositiveIntegerField(choices=[(0, 'NMR'), (1, 'X_Ray C'), (2, 'Cryo-EM')])),
                ('uniprot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.UniprotKb')),
            ],
        ),
    ]
