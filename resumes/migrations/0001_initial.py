# Generated by Django 3.0.5 on 2020-05-11 11:48

from django.db import migrations, models
import resumes.views


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('birth', models.DateField()),
                ('phonenumber', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail')),
                ('job', models.CharField(max_length=10)),
                ('native', models.CharField(max_length=30)),
                ('politic', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30)),
                ('rank', models.CharField(max_length=30)),
                ('intake', models.CharField(max_length=30)),
                ('graduation_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Jobintansion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=20)),
                ('postion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Procedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_on', models.DateField()),
                ('time_off', models.DateField()),
                ('achievements', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rewarded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize', models.CharField(max_length=20)),
                ('winningtime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField(max_length=200)),
                ('selfassessment', models.TextField(max_length=200)),
                ('sublication', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workexperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corporation', models.CharField(max_length=30)),
                ('procedules', models.ForeignKey(blank=True, null=True, on_delete=resumes.views.CASCADE, to='resumes'
                                                                                                            '.Procedules')),
            ],
        ),
        migrations.CreateModel(
            name='Schooltime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('association', models.CharField(max_length=30)),
                ('procedules', models.ForeignKey(blank=True, null=True, on_delete=resumes.views.CASCADE, to='resumes.Procedules')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corporation', models.CharField(max_length=30)),
                ('procedules', models.ForeignKey(blank=True, null=True, on_delete=resumes.views.CASCADE, to='resumes.Procedules')),
            ],
        ),
    ]