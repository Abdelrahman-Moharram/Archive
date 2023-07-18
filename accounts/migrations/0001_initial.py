# Generated by Django 4.2.3 on 2023-07-15 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fullname', models.CharField(max_length=20, verbose_name='Full Name')),
                ('militry_id', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('moahl', models.CharField(max_length=150, null=True)),
                ('tagned_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Moahl_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('duration', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Work_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users_Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='moahl_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.moahl_type'),
        ),
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.rank'),
        ),
        migrations.AddField(
            model_name='user',
            name='work_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.work_category'),
        ),
    ]