# Generated by Django 4.0.5 on 2022-06-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default='No link present'),
            preserve_default=False,
        ),
    ]