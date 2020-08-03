# Generated by Django 3.0.8 on 2020-08-02 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theapi', '0002_remove_person_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='City',
            field=models.OneToOneField(default=1.0, on_delete=django.db.models.deletion.CASCADE, to='theapi.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='Town',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='theapi.Town'),
        ),
    ]
