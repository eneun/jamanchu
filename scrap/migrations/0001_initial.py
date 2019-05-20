# Generated by Django 2.1.7 on 2019-05-20 18:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meeting', '0002_meeting_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meeting', models.ForeignKey(on_delete=True, related_name='meetings', to='meeting.Meeting')),
                ('user', models.ForeignKey(on_delete=True, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
