# Generated by Django 4.0.4 on 2023-12-15 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_isnew_card_topic_alter_card_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='source',
            field=models.CharField(default='NAN', max_length=40),
        ),
    ]
