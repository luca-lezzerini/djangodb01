# Generated by Django 5.1.3 on 2024-11-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbexample', '0003_course_credits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
            ],
        ),
    ]
