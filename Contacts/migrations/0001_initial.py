# Generated by Django 3.1.4 on 2021-01-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, help_text='Name of sender', max_length=20, null=True)),
                ('email', models.EmailField(editable=False, max_length=50, null=True)),
                ('subject', models.CharField(editable=False, max_length=100, null=True)),
                ('message', models.TextField(editable=False, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]
