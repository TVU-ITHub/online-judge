# Generated by Django 3.2.19 on 2024-09-05 01:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0205_ip_based_auth'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationMonthlyUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(verbose_name='time')),
                ('consumed_credit', models.FloatField(default=0, verbose_name='consumed credit')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_usages', to='judge.organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'organization monthly usage',
                'verbose_name_plural': 'organization monthly usages',
                'unique_together': {('organization', 'time')},
            },
        ),
    ]
