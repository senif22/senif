# Generated by Django 4.2.3 on 2023-08-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_no', models.IntegerField()),
                ('roll_no', models.IntegerField()),
                ('enr_no', models.IntegerField()),
                ('name', models.TextField()),
                ('div', models.TextField()),
                ('pro_det', models.TextField()),
            ],
            options={
                'db_table': 'project_detail',
            },
        ),
        migrations.DeleteModel(
            name='todolistitem',
        ),
    ]
