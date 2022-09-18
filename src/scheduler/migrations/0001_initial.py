# Generated by Django 4.1.1 on 2022-09-18 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('beds', models.IntegerField()),
                ('imc_beds', models.IntegerField()),
                ('required_charge', models.IntegerField(default=1)),
                ('required_nurses', models.IntegerField()),
                ('required_techs', models.IntegerField()),
                ('nurse_ratio', models.IntegerField()),
                ('imc_ratio', models.IntegerField()),
                ('tech_ration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('worker_off', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker', models.CharField(choices=[('NU', 'Nurse'), ('TE', 'Technician')], max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('shift', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Hybrid', 'Hybrid')], max_length=30)),
                ('hours', models.IntegerField()),
                ('shift_length', models.IntegerField()),
                ('holidays', models.ManyToManyField(to='scheduler.holiday')),
            ],
        ),
    ]