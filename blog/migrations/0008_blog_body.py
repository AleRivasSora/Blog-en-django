# Generated by Django 3.0 on 2020-02-11 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default=django.utils.timezone.now, verbose_name={'cols': 15, 'rows': 4}),
            preserve_default=False,
        ),
    ]