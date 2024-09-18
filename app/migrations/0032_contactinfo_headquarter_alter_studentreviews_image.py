# Generated by Django 4.2.13 on 2024-09-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_rename_first_name_studentreviews_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('phone1', models.CharField(blank=True, max_length=255, null=True)),
                ('phone2', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'ContactInfo',
                'verbose_name_plural': 'ContactInfo',
            },
        ),
        migrations.CreateModel(
            name='Headquarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text1', models.CharField(blank=True, max_length=255, null=True)),
                ('text2', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Headquarter',
                'verbose_name_plural': 'Headquarter',
            },
        ),
        migrations.AlterField(
            model_name='studentreviews',
            name='image',
            field=models.ImageField(upload_to='studentreviews'),
        ),
    ]