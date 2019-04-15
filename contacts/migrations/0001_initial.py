# Generated by Django 2.2 on 2019-04-15 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.IntegerField(null=True)),
                ('phone_no', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
    ]
