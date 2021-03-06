# Generated by Django 3.1 on 2021-08-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210816_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content_html',
            field=models.TextField(verbose_name='内容html格式'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content_md',
            field=models.TextField(verbose_name='内容markdown格式'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='阅读数'),
        ),
        migrations.AlterField(
            model_name='category',
            name='citations',
            field=models.IntegerField(default=0, verbose_name='引用次数'),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=16, verbose_name='分类名'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='citations',
            field=models.IntegerField(default=0, verbose_name='引用次数'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=16, verbose_name='标签名'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
