# Generated by Django 2.2.4 on 2019-09-18 09:57

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190918_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
