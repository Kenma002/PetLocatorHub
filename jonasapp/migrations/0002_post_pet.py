# Generated by Django 4.2.6 on 2024-01-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jonasapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pet',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat')], default='dog', max_length=80),
        ),
    ]
