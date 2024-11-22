# Generated by Django 4.2.4 on 2024-11-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='earn',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='family',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='know',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='patience',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='risk',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='saving',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='term',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
