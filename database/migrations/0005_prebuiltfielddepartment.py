# Generated by Django 5.0.2 on 2024-04-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_prebuiltfield_options_databasefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreBuiltFieldDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='اسم القسم')),
            ],
            options={
                'verbose_name': 'قسم',
                'verbose_name_plural': 'اقسام الحقول المسبقة',
            },
        ),
    ]
