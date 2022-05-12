# Generated by Django 3.1.7 on 2022-05-11 12:12

from django.db import migrations, models
import django.forms.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20211102_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default='0')),
                ('profit', models.FloatField(default=0)),
                ('position_size', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='SOME STRING', max_length=100)),
                ('price_in', models.FloatField(default=0)),
                ('time_in', models.DateTimeField(default=django.forms.widgets.DateTimeInput)),
                ('order_type', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='SOME STRING', max_length=100)),
                ('price_in', models.FloatField(default=0)),
                ('time_in', models.DateTimeField(default=django.forms.widgets.DateTimeInput)),
                ('order_type', models.CharField(default='SOME STRING', max_length=100)),
                ('current_pl', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='BOT',
        ),
        migrations.DeleteModel(
            name='BOT1',
        ),
        migrations.DeleteModel(
            name='BOT2',
        ),
        migrations.DeleteModel(
            name='BOT3',
        ),
        migrations.DeleteModel(
            name='BOT4',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='account_num',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='angel_API_keys',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='angel_password',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='angel_username',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='another_referral',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='ifsc',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='referral',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='security',
        ),
        migrations.AddField(
            model_name='user1',
            name='group',
            field=models.IntegerField(default='0'),
        ),
    ]
