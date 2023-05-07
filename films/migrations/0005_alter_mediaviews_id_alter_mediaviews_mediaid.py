# Generated by Django 4.1 on 2023-05-07 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_mediaviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaviews',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mediaviews',
            name='mediaId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.media'),
        ),
    ]
