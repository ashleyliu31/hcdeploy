# Generated by Django 2.1.5 on 2019-02-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cross_currents',
            fields=[
                ('ArticleID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=500)),
                ('Author', models.CharField(max_length=200, null=True)),
                ('Journal', models.CharField(max_length=500, null=True)),
                ('Pub_Year', models.IntegerField(null=True)),
                ('Issue', models.IntegerField(null=True)),
                ('Link', models.URLField(max_length=800, null=True)),
                ('Content', models.TextField()),
            ],
            options={
                'db_table': 'cross_currents',
            },
        ),
        migrations.CreateModel(
            name='cross_currents_article_detail',
            fields=[
                ('ArticleID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=500)),
                ('Author', models.CharField(max_length=200, null=True)),
                ('Journal', models.CharField(max_length=500, null=True)),
                ('Pub_Year', models.IntegerField(null=True)),
                ('Issue', models.IntegerField(null=True)),
                ('Link', models.URLField(max_length=800, null=True)),
                ('Content', models.TextField()),
            ],
            options={
                'db_table': 'cross_currents',
            },
        ),
    ]
