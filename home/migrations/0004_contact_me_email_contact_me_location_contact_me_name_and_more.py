# Generated by Django 4.2.4 on 2023-08-26 05:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_me_about_me_image_alter_blog_me_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_me',
            name='email',
            field=models.EmailField(default='makhmudx965pa@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contact_me',
            name='location',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contact_me',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contact_me',
            name='telephone',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='aboutme_text',
            field=ckeditor.fields.RichTextField(default=True),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='email',
            field=models.EmailField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='ismim',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='men_kimligim',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='region',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='yoshim',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='blog_me',
            name='image',
            field=models.ImageField(default=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='blog_me',
            name='text',
            field=ckeditor.fields.RichTextField(default=True),
        ),
        migrations.AlterField(
            model_name='blog_me',
            name='title',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contact_me',
            name='title',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
