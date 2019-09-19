# Generated by Django 2.2.3 on 2019-07-15 14:44

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0106_auto_20190715_1622")]

    operations = [
        migrations.AlterField(
            model_name="besluittype",
            name="catalogus",
            field=models.ForeignKey(
                help_text="URL-referentie naar de CATALOGUS waartoe dit BESLUITTYPE behoort.",
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.Catalogus",
                verbose_name="catalogus",
            ),
        ),
        migrations.AlterField(
            model_name="besluittype",
            name="informatieobjecttypes",
            field=models.ManyToManyField(
                blank=True,
                help_text="URL-referenties naar het INFORMATIEOBJECTTYPE van informatieobjecten waarin besluiten van dit BESLUITTYPE worden vastgelegd.",
                to="datamodel.InformatieObjectType",
                verbose_name="informatieobjecttype",
            ),
        ),
        migrations.AlterField(
            model_name="eigenschap",
            name="zaaktype",
            field=models.ForeignKey(
                help_text="URL-referentie naar het ZAAKTYPE van de ZAAKen waarvoor deze EIGENSCHAP van belang is.",
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.ZaakType",
                verbose_name="is van",
            ),
        ),
        migrations.AlterField(
            model_name="eigenschapspecificatie",
            name="waardenverzameling",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    max_length=100, verbose_name="waardenverzameling"
                ),
                blank=True,
                help_text="Waarden die deze EIGENSCHAP kan hebben.",
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="informatieobjecttype",
            name="catalogus",
            field=models.ForeignKey(
                help_text="URL-referentie naar de CATALOGUS waartoe dit INFORMATIEOBJECTTYPE behoort.",
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.Catalogus",
                verbose_name="maakt deel uit van",
            ),
        ),
        migrations.AlterField(
            model_name="mogelijkebetrokkene",
            name="betrokkene",
            field=models.URLField(
                help_text="URL-referentie naar een specifieke BETROKKENE die kan gerelateerd worden aan een ZAAK."
            ),
        ),
        migrations.AlterField(
            model_name="mogelijkebetrokkene",
            name="betrokkene_type",
            field=models.CharField(
                choices=[
                    ("natuurlijk_persoon", "Natuurlijk persoon"),
                    ("niet_natuurlijk_persoon", "Niet-natuurlijk persoon"),
                    ("vestiging", "Vestiging"),
                    ("organisatorische_eenheid", "Organisatorische eenheid"),
                    ("medewerker", "Medewerker"),
                ],
                help_text="Het type BETROKKENE waarnaar verwezen wordt in het attribuut `betrokkene`.",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="resultaattype",
            name="selectielijstklasse",
            field=models.URLField(
                help_text="URL-referentie naar de, voor het archiefregime bij het RESULTAATTYPE relevante, categorie in de Selectielijst Archiefbescheiden (RESULTAAT in de Selectielijst API) van de voor het ZAAKTYPE verantwoordelijke overheidsorganisatie.",
                max_length=1000,
                verbose_name="selectielijstklasse",
            ),
        ),
        migrations.AlterField(
            model_name="resultaattype",
            name="zaaktype",
            field=models.ForeignKey(
                help_text="URL-referentie naar het ZAAKTYPE van ZAAKen waarin resultaten van dit RESULTAATTYPE bereikt kunnen worden.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resultaattypen",
                to="datamodel.ZaakType",
                verbose_name="is relevant voor",
            ),
        ),
        migrations.AlterField(
            model_name="roltype",
            name="zaaktype",
            field=models.ForeignKey(
                help_text="URL-referentie naar het ZAAKTYPE waar deze ROLTYPEn betrokken kunnen zijn.",
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.ZaakType",
                verbose_name="is van",
            ),
        ),
        migrations.AlterField(
            model_name="statustype",
            name="zaaktype",
            field=models.ForeignKey(
                help_text="URL-referentie naar het ZAAKTYPE van ZAAKen waarin STATUSsen van dit STATUSTYPE bereikt kunnen worden.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="statustypen",
                to="datamodel.ZaakType",
                verbose_name="is van",
            ),
        ),
        migrations.AlterField(
            model_name="zaakinformatieobjecttype",
            name="informatieobjecttype",
            field=models.ForeignKey(
                help_text="URL-referentie naar het INFORMATIEOBJECTTYPE.",
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.InformatieObjectType",
                verbose_name="informatie object type",
            ),
        ),
        migrations.AlterField(
            model_name="zaakinformatieobjecttype",
            name="statustype",
            field=models.ForeignKey(
                blank=True,
                help_text="URL-referentie naar het STATUSTYPE waarbij deze INFORMATIEOBJECTTYPEn verplicht aanwezig moeten zijn.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="heeft_verplichte_zit",
                to="datamodel.StatusType",
                verbose_name="status type",
            ),
        ),
        migrations.AlterField(
            model_name="zaakinformatieobjecttype",
            name="volgnummer",
            field=models.PositiveSmallIntegerField(
                help_text="Uniek volgnummer van het ZAAK-INFORMATIEOBJECTTYPE binnen het ZAAKTYPE.",
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(999),
                ],
                verbose_name="volgnummer",
            ),
        ),
        migrations.AlterField(
            model_name="zaakinformatieobjecttype",
            name="zaaktype",
            field=models.ForeignKey(
                help_text="URL-referentie naar het ZAAKTYPE.",
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.ZaakType",
                verbose_name="zaaktype",
            ),
        ),
        migrations.AlterField(
            model_name="zaaktype",
            name="catalogus",
            field=models.ForeignKey(
                help_text="URL-referentie naar de CATALOGUS waartoe dit ZAAKTYPE behoort.",
                on_delete=django.db.models.deletion.CASCADE,
                to="datamodel.Catalogus",
                verbose_name="maakt deel uit van",
            ),
        ),
        migrations.AlterField(
            model_name="zaaktype",
            name="selectielijst_procestype",
            field=models.URLField(
                blank=True,
                help_text="URL-referentie naar een vanuit archiveringsoptiek onderkende groep processen met dezelfde kenmerken (PROCESTYPE in de Selectielijst API).",
                verbose_name="selectielijst procestype",
            ),
        ),
    ]
