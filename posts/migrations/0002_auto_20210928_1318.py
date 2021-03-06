# Generated by Django 3.2.7 on 2021-09-28 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangePostDeliveryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book1title', models.CharField(default=None, max_length=250, null=True)),
                ('book1author', models.CharField(default=None, max_length=250, null=True)),
                ('book2title', models.CharField(default=None, max_length=250, null=True)),
                ('book2author', models.CharField(default=None, max_length=250, null=True)),
                ('book1DeliveryAddress', models.CharField(default=None, max_length=255, null=True)),
                ('book2DeliveryAddress', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='PostImage',
            new_name='ExchangePostImage',
        ),
        migrations.AddField(
            model_name='exchangepost',
            name='setVisible',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offeredUserAddr', models.CharField(max_length=255)),
                ('offered', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='offered', to='posts.exchangepost')),
                ('offeredUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offeredUser', to=settings.AUTH_USER_MODEL)),
                ('offeringFor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='offeringFor', to='posts.exchangepost')),
                ('offeringForUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offeringForUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
