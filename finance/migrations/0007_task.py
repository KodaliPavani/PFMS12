# Generated by Django 5.1.4 on 2024-12-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_spending'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
