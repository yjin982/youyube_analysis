# Generated by Django 3.0.6 on 2020-07-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=20, null=True)),
                ('ip', models.CharField(blank=True, max_length=20, null=True)),
                ('pw', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(blank=True, db_column='DATE', null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoardComment',
            fields=[
                ('board_comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=20, null=True)),
                ('ip', models.CharField(blank=True, max_length=20, null=True)),
                ('pw', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(blank=True, db_column='DATE', null=True)),
            ],
            options={
                'db_table': 'board_comment',
                'managed': False,
            },
        ),
    ]
