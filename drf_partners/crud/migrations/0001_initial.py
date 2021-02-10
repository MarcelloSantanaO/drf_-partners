# Generated by Django 3.1.6 on 2021-02-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('partnership_status', models.CharField(default='Not Initiated', max_length=20)),
                ('uf', models.CharField(max_length=2)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('cnpj_status', models.CharField(max_length=50)),
            ],
        ),
    ]
