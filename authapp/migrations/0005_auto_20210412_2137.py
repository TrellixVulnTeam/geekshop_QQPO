# Generated by Django 3.1.7 on 2021-04-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_shopuserprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users_avatars'),
        ),
    ]