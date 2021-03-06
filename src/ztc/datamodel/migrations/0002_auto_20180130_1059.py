# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 09:59
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="broncatalogus", options={"verbose_name_plural": "Bron Catalogussen"}
        ),
        migrations.AlterModelOptions(
            name="formulier", options={"verbose_name_plural": "Formulieren"}
        ),
        migrations.AlterModelOptions(
            name="productdienst", options={"verbose_name_plural": "Product / Diensten"}
        ),
        migrations.AlterModelOptions(
            name="referentieproces",
            options={"verbose_name_plural": "Referentieprocessen"},
        ),
        migrations.AlterField(
            model_name="eigenschapspecificatie",
            name="waardenverzameling",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    max_length=100, verbose_name="waardenverzameling"
                ),
                blank=True,
                help_text="Waarden die deze EIGENSCHAP kan hebben (Gebruik een komma om waarden van elkaar te onderscheiden.)",
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="informatieobjecttype",
            name="informatieobjecttypetrefwoord",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=30, verbose_name="trefwoord"),
                blank=True,
                help_text="Trefwoord(en) waarmee informatieobjecten van het INFORMATIEOBJECTTYPE kunnen worden gekarakteriseerd. (Gebruik een komma om waarden van elkaar te onderscheiden.)",
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="informatieobjecttype",
            name="model",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.URLField(verbose_name="model"),
                blank=True,
                help_text="De URL naar het model / sjabloon dat wordt gebruikt voor de creatie van informatieobjecten van dit INFORMATIEOBJECTTYPE. (Gebruik een komma om waarden van elkaar te onderscheiden.)",
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="roltype",
            name="soort_betrokkene",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    max_length=80, verbose_name="soort betrokkene"
                ),
                help_text="De (soort) betrokkene die een rol van dit roltype mag uitoefenen. (Gebruik een komma om waarden van elkaar te onderscheiden.)",
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="zaaktype",
            name="trefwoord",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=30, verbose_name="trefwoord"),
                blank=True,
                help_text="Een trefwoord waarmee ZAAKen van het ZAAKTYPE kunnen worden gekarakteriseerd.(Gebruik een komma om waarden van elkaar te onderscheiden.)",
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="zaaktype",
            name="verantwoordingsrelatie",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    max_length=40, verbose_name="verantwoordingsrelatie"
                ),
                blank=True,
                help_text="De relatie tussen ZAAKen van dit ZAAKTYPE en de beleidsmatige en/of financiële verantwoording. (Gebruik een komma om waarden van elkaar te onderscheiden.)",
                size=None,
            ),
        ),
    ]
