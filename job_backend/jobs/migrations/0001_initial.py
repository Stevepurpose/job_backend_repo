# Generated by Django 4.2.16 on 2024-11-21 02:20

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
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('role', models.CharField(max_length=255, verbose_name='Role')),
                ('applied', models.BooleanField(default=False, verbose_name='Applied')),
                ('Discussions', models.TextField(default=False)),
                ('offer', models.BooleanField(default=False, verbose_name='Offer')),
                ('advert_start', models.DateTimeField(verbose_name='Advert Date')),
                ('close_date', models.DateTimeField(null=True, verbose_name='Advert Closes')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['company_name'],
            },
        ),
    ]
