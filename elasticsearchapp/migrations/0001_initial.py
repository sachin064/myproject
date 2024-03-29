# Generated by Django 2.2.6 on 2019-10-10 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogpost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
