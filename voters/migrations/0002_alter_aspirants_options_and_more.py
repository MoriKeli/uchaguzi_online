# Generated by Django 4.1.2 on 2022-10-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aspirants',
            options={'ordering': ['name'], 'verbose_name_plural': 'Aspirants'},
        ),
        migrations.RenameField(
            model_name='aspirants',
            old_name='aspirant',
            new_name='name',
        ),
        migrations.AddField(
            model_name='aspirants',
            name='alias',
            field=models.CharField(blank=True, default='alias', max_length=25),
        ),
        migrations.AddField(
            model_name='voters',
            name='reg_no',
            field=models.CharField(default='1', max_length=14),
        ),
        migrations.AlterField(
            model_name='voters',
            name='age',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='voters',
            name='school',
            field=models.CharField(max_length=70),
        ),
    ]
