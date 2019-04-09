# Generated by Django 2.0.9 on 2019-01-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0044_auto_20190108_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaaktype',
            name='opschorting_aanhouding_mogelijk',
            field=models.CharField(choices=[('J', 'Ja'), ('N', 'Nee')], help_text='Aanduiding die aangeeft of ZAAKen van dit mogelijk ZAAKTYPE kunnen worden opgeschort en/of aangehouden.', max_length=5, verbose_name='opschorting/aanhouding mogelijk'),
        ),
        migrations.AlterField(
            model_name='zaaktype',
            name='publicatie_indicatie',
            field=models.CharField(choices=[('J', 'Ja'), ('N', 'Nee')], help_text='Aanduiding of (het starten van) een ZAAK van AN1 dit ZAAKTYPE gepubliceerd moet worden.', max_length=5, verbose_name='publicatie indicatie'),
        ),
        migrations.AlterField(
            model_name='zaaktype',
            name='verlenging_mogelijk',
            field=models.CharField(choices=[('J', 'Ja'), ('N', 'Nee')], help_text='Aanduiding die aangeeft of de Doorlooptijd behandeling van ZAAKen van dit ZAAKTYPE kan worden verlengd.', max_length=5, verbose_name='verlenging mogelijk'),
        ),
    ]