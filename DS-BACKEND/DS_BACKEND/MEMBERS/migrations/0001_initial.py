# Generated by Django 4.2.2 on 2023-07-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(blank=True, null=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(blank=True, default='', max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('passout_year', models.CharField(default='2017', max_length=10)),
                ('dp', models.ImageField(blank=True, null=True, upload_to='alumniDPs/')),
                ('facebook_url', models.URLField(blank=True, max_length=300, null=True)),
                ('instagram_url', models.URLField(blank=True, max_length=300, null=True)),
                ('linkedin_url', models.URLField(blank=True, max_length=300, null=True)),
                ('github_url', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(blank=True, null=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('year', models.CharField(choices=[('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], default='Second', max_length=10)),
                ('post', models.CharField(blank=True, default='Senior Member', max_length=100, null=True)),
                ('dp', models.ImageField(blank=True, null=True, upload_to='memberDPs/')),
                ('instagram_url', models.URLField(blank=True, max_length=300, null=True)),
                ('linkedin_url', models.URLField(blank=True, max_length=300, null=True)),
                ('facebook_url', models.URLField(blank=True, max_length=300, null=True)),
                ('github_url', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
