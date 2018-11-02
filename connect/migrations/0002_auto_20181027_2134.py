# Generated by Django 2.1.2 on 2018-10-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('tel_num', models.CharField(max_length=50)),
                ('about', models.TextField(help_text='Описание')),
                ('time_reg', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='bulletion',
            old_name='_id',
            new_name='_id1',
        ),
    ]
