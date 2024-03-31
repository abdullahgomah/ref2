# Generated by Django 5.0.2 on 2024-03-29 23:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='اسم الموقع')),
                ('ui', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='ملفات واجهة المستخدم')),
            ],
            options={
                'verbose_name': 'موقع',
                'verbose_name_plural': 'المواقع',
            },
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='اسم بيئة العمل')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'بيئة عمل',
                'verbose_name_plural': 'بيئات العمل',
            },
        ),
        migrations.CreateModel(
            name='WebsitePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='اسم الصفحة')),
                ('code', models.TextField(verbose_name='الكود')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='workspace.website', verbose_name='الموقع')),
            ],
            options={
                'verbose_name': 'صفحة موقع',
                'verbose_name_plural': 'صفحات المواقع',
            },
        ),
        migrations.AddField(
            model_name='website',
            name='workspace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='websites', to='workspace.workspace'),
        ),
    ]
