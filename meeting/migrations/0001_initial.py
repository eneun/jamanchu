# Generated by Django 2.1.7 on 2019-05-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('식사', '식사'), ('문화', '문화'), ('스포츠/레저', '스포츠/레저'), ('취미/힐링', '취미/힐링'), ('스터디', '스터디'), ('기타', '기타')], max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
