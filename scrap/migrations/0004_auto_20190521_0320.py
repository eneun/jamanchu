# Generated by Django 2.1.7 on 2019-05-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0003_auto_20190521_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='meeting',
            field=models.ForeignKey(on_delete=True, related_name='scrapped', to='meeting.Meeting', unique=True),
        ),
    ]
