# Generated by Django 4.1.3 on 2023-01-16 13:12

import core.models.coordinate
import core.models.gallery
from django.db import migrations, models
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('file', models.FileField(default='users/coordinates/blank_json.json', upload_to=core.models.coordinate.coordinate_directory_path, verbose_name='file')),
                ('x', models.CharField(blank=True, max_length=30, verbose_name='x coordinate')),
                ('y', models.CharField(blank=True, max_length=30, verbose_name='y coordinate')),
                ('x2', models.CharField(blank=True, max_length=30, verbose_name='x2 coordinate')),
                ('y2', models.CharField(blank=True, max_length=30, verbose_name='y2 coordinate')),
                ('file_created', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Coordinates',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('file', models.FileField(default='gallery/default_image.png', upload_to=core.models.gallery.gallery_directory_path, verbose_name='file')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
                'ordering': ['-created'],
            },
        ),
    ]
