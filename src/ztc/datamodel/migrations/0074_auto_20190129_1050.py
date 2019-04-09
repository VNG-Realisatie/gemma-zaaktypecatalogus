# Generated by Django 2.0.9 on 2019-01-29 09:50

from django.db import migrations
import vng_api_common.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0073_auto_20190117_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaaktype',
            name='verlengingstermijn',
            field=vng_api_common.fields.DaysDurationField(blank=True, help_text='De termijn in dagen waarmee de Doorlooptijd behandeling van ZAAKen van dit ZAAKTYPE kan worden verlengd.', max_duration=999, min_duration=1, null=True, verbose_name='verlengingstermijn'),
        ),
    ]