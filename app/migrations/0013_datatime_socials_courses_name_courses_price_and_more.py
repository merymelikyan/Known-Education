# Generated by Django 5.1 on 2024-09-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_about_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar', models.DateTimeField(blank=True, max_length=20, null=True)),
                ('html_calendar', models.CharField(max_length=255)),
                ('clock', models.DateTimeField(blank=True, max_length=20, null=True)),
                ('html_clock', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'DataTime',
                'verbose_name_plural': 'Datatimes',
            },
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, max_length=255)),
                ('html_class', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='about',
            name='icon',
            field=models.CharField(blank=True, help_text='FontAwesome icon', max_length=50, null=True),
        ),
    ]
