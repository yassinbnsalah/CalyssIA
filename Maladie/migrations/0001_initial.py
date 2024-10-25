# Generated by Django 4.1.13 on 2024-10-19 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Maladie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True, verbose_name='Nom de la maladie')),
                ('description', models.TextField(verbose_name='Description de la maladie')),
                ('image', models.ImageField(blank=True, null=True, upload_to='maladies/', verbose_name='Image de la maladie')),
                ('causes', models.TextField(blank=True, verbose_name='Causes de la maladie')),
                ('symptomes', models.TextField(blank=True, verbose_name='Symptomes observables')),
                ('date_publication', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maladies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Maladie',
                'verbose_name_plural': 'Maladies',
                'ordering': ['-date_publication'],
            },
        ),
    ]