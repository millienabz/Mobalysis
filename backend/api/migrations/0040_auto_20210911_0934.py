# Generated by Django 3.1.2 on 2021-09-11 09:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0039_merge_20210911_0930"),
    ]

    operations = [
        migrations.AlterField(
            model_name="spell",
            name="effect",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.ArrayField(
                    base_field=models.IntegerField(), size=None
                ),
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="spell",
            name="effectBurn",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=200, null=True),
                default="",
                null=True,
                size=None,
            ),
        ),
    ]