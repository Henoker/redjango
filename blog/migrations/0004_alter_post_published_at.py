# Generated by Django 5.0.3 on 2024-04-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment_created_at_comment_modified_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_at",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
