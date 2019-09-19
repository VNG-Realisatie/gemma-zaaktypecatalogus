# Generated by Django 2.0.10 on 2019-02-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0091_auto_20190226_1416")]

    operations = [
        migrations.AlterField(
            model_name="resultaattype",
            name="archiefactietermijn",
            field=models.DurationField(
                blank=True,
                help_text="De termijn, na het vervallen van het bedrjfsvoeringsbelang, waarna het zaakdossier (de ZAAK met alle bijbehorende INFORMATIEOBJECTen) van een ZAAK met een resultaat van dit RESULTAATTYPE vernietigd of overgebracht (naar een archiefbewaarplaats) moet worden. Voor te vernietigen dossiers betreft het de in die Selectielijst genoemde bewaartermjn. Voor blijvend te bewaren zaakdossiers betreft het de termijn vanaf afronding van de zaak tot overbrenging (de procestermijn is dan nihil).",
                null=True,
                verbose_name="archiefactietermijn",
            ),
        ),
        migrations.AlterField(
            model_name="resultaattype",
            name="brondatum_archiefprocedure_objecttype",
            field=models.CharField(
                blank=True,
                choices=[
                    ("VerblijfsObject", "Verblijfsobject"),
                    ("MeldingOpenbareRuimte", "Melding openbare ruimte"),
                    ("InzageVerzoek", "Inzage verzoek in het kader van de AVG"),
                ],
                help_text="Het soort object in de registratie dat het procesobject representeert.",
                max_length=80,
                verbose_name="objecttype",
            ),
        ),
    ]
