# Generated by Django 3.1.5 on 2021-05-18 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='markc',
            new_name='MarksInChemistry',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='markm',
            new_name='MarksInMathematics',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='markp',
            new_name='MarksInPhysics',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='percentage',
            new_name='Percentage',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='roll_no',
            new_name='Roll_no',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='total',
            new_name='Total',
        ),
    ]
