# Generated by Django 4.1.3 on 2022-11-25 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirants',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('alias', models.CharField(blank=True, max_length=25)),
                ('bio', models.TextField()),
                ('post', models.CharField(max_length=32)),
                ('slogan', models.CharField(blank=True, max_length=50)),
                ('pic', models.ImageField(upload_to='Aspirant-Dps/')),
                ('form', models.FileField(upload_to='Nomination-Forms/')),
                ('nominate', models.BooleanField(default=False)),
                ('votes', models.PositiveIntegerField(default=0, editable=False)),
                ('applied', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Aspirants',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.CharField(editable=False, max_length=18, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.CharField(editable=False, max_length=20)),
                ('academic', models.BooleanField(default=False, editable=False)),
                ('general_rep', models.BooleanField(default=False, editable=False)),
                ('ladies_rep', models.BooleanField(default=False, editable=False)),
                ('treasurer', models.BooleanField(default=False, editable=False)),
                ('governor', models.BooleanField(default=False, editable=False)),
                ('president', models.BooleanField(default=False, editable=False)),
                ('polled', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Voted',
            },
        ),
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('gender', models.CharField(max_length=7)),
                ('phone_no', models.CharField(max_length=14)),
                ('age', models.PositiveIntegerField(default=0, editable=False)),
                ('dob', models.DateField(null=True)),
                ('profile_pic', models.ImageField(default='default.png', upload_to='VotersDps/')),
                ('reg_no', models.CharField(max_length=14)),
                ('school', models.CharField(max_length=70)),
                ('year', models.CharField(max_length=12)),
                ('semester', models.CharField(max_length=1)),
                ('registered', models.BooleanField(default=False, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('voter', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Voters',
                'ordering': ['voter'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('written', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('blogger', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='voters.aspirants')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'ordering': ['written'],
            },
        ),
        migrations.AddField(
            model_name='aspirants',
            name='name',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='voters.voters'),
        ),
    ]
