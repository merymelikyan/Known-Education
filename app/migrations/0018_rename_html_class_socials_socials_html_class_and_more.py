# Generated by Django 5.1 on 2024-09-05 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_teamblock_social_html_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socials',
            old_name='html_class',
            new_name='socials_html_class',
        ),
        migrations.RemoveField(
            model_name='teamblock',
            name='social_html_class',
        ),
        migrations.RemoveField(
            model_name='teamblock',
            name='social_title',
        ),
        migrations.RemoveField(
            model_name='teamblock',
            name='social_url',
        ),
    ]
