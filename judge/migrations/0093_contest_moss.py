# Generated by Django 2.1.12 on 2019-10-17 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0092_contest_clone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestMoss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=10)),
                ('submission_count', models.PositiveIntegerField(default=0)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'contest moss result',
                'verbose_name_plural': 'contest moss results',
            },
        ),
        migrations.AlterModelOptions(
            name='contest',
            options={'permissions': (('see_private_contest', 'See private contests'), ('edit_own_contest', 'Edit own contests'), ('edit_all_contest', 'Edit all contests'), ('clone_contest', 'Clone contest'), ('moss_contest', 'MOSS contest'), ('contest_rating', 'Rate contests'), ('contest_access_code', 'Contest access codes'), ('create_private_contest', 'Create private contests')), 'verbose_name': 'contest', 'verbose_name_plural': 'contests'},
        ),
        migrations.AddField(
            model_name='contestmoss',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moss', to='judge.Contest', verbose_name='contest'),
        ),
        migrations.AddField(
            model_name='contestmoss',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moss', to='judge.Problem', verbose_name='problem'),
        ),
        migrations.AlterUniqueTogether(
            name='contestmoss',
            unique_together={('contest', 'problem', 'language')},
        ),
    ]
