# Generated by Django 2.1.5 on 2019-05-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='deleted',
            field=models.DateField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
    ]
