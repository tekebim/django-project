# Generated by Django 3.1.4 on 2020-12-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('is_done', models.BooleanField()),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
