# Generated by Django 3.0.8 on 2020-08-02 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('Population', models.IntegerField()),
                ('GDP', models.FloatField()),
                ('PinCode', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, unique=True)),
                ('Description', models.TextField()),
                ('Population', models.IntegerField()),
                ('GDP', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, unique=True)),
                ('Description', models.TextField()),
                ('Population', models.IntegerField()),
                ('GDP', models.FloatField()),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapi.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('Population', models.IntegerField()),
                ('GDP', models.FloatField()),
                ('PinCode', models.CharField(max_length=200)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapi.Country')),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapi.State')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapi.City')),
                ('Town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapi.Town')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='Country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapi.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapi.State'),
        ),
    ]
