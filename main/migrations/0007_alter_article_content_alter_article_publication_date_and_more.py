# Generated by Django 5.0.6 on 2024-06-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_article_content_alter_article_publication_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=1000, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='publication date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
    ]
