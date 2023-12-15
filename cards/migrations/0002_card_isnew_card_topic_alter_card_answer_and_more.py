# Generated by Django 4.0.4 on 2023-12-07 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='isNew',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='card',
            name='topic',
            field=models.CharField(choices=[('Phonetics', 'Phonetics'), ('Phonology', 'Phonology'), ('Morphology', 'Morphology'), ('Syntax', 'Syntax'), ('Semantics', 'Semantics'), ('Pragmatics', 'Pragmatics')], default='Phonetics', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='answer',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='card',
            name='box',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Easy', max_length=10),
        ),
        migrations.AlterField(
            model_name='card',
            name='question',
            field=models.CharField(max_length=300),
        ),
    ]
