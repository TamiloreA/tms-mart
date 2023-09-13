# Generated by Django 4.2.4 on 2023-09-13 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_post_author_alter_post_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(max_length=400, null=True)),
                ('slug', models.SlugField(null=True)),
                ('date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.author')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]