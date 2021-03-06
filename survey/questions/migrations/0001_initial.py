# Generated by Django 2.2.6 on 2019-10-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('type_questions', models.CharField(choices=[('text', 'Text'), ('selection', 'Selection'), ('multiple', 'Multiple')], default='text', max_length=20)),
                ('isRequired', models.BooleanField(default=False)),
            ],
        ),
    ]
