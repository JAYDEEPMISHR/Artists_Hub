# Generated by Django 4.2.1 on 2023-06-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
    ]