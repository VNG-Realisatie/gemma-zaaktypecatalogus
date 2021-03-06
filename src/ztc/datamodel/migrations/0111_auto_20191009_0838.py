# Generated by Django 2.2.4 on 2019-10-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0110_auto_20190729_1041")]

    operations = [
        migrations.AddField(
            model_name="besluittype",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="catalogus",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="eigenschap",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="informatieobjecttype",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="informatieobjecttypeomschrijvinggeneriek",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="resultaattype",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="roltype",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="statustype",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="zaakinformatieobjecttype",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="zaaktype",
            name="_etag",
            field=models.CharField(
                default="",
                editable=False,
                help_text="MD5 hash of the resource representation in its current version.",
                max_length=32,
                verbose_name="etag value",
            ),
            preserve_default=False,
        ),
    ]
