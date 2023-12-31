# Generated by Django 4.2.3 on 2023-07-20 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_alter_tamam_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qeta3_Nadafa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weight', models.FloatField()),
                ('is_main', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tamam',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tamam',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tamam',
            name='tamam_asasy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='home.tamam_asasy'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Daily_Nadafa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('qeta3_nadafa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.qeta3_nadafa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
