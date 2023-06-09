# Generated by Django 3.2.19 on 2023-06-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_vacancy_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='area',
            field=models.CharField(choices=[('IRELAND', 'Ireland'), ('DUBLIN_CITY', 'Dublin'), ('DUBLIN_CITY_CENTRE', 'Dublin City Centre'), ('DUBLIN_NORTH', 'Dublin North'), ('DUBLIN_SOUTH', 'Dublin South'), ('DUBLIN_WEST', 'Dublin West'), ('DUBLIN_COUNTY', 'co. Dublin'), ('CARLOW', 'co. Carlow'), ('CAVAN', 'co. Cavan'), ('CLARE', 'co. Clare'), ('CORK_CITY', 'Cork'), ('CORK_COUNTY', 'co. Cork'), ('DONEGAL', 'co. Donegal'), ('GALWAY_CITY', 'Galway'), ('GALWAY_COUNTY', 'co. Galway'), ('KERRY', 'co. Kerry'), ('KILDARE', 'co. Kildare'), ('KILKENNY_CITY', 'Kilkenny'), ('KILKENNY_COUNTY', 'co. Kilkenny'), ('LAOIS', 'co. Laois'), ('LEITRIM', 'co. Leitrim'), ('LIMERICK_CITY', 'Limerick'), ('LIMERICK_COUNTY', 'co. Limerick'), ('LONGFORD', 'co. Longford'), ('LOUTH', 'co. Louth'), ('MAYO', 'co. Mayo'), ('MEATH', 'co. Meath'), ('MONAGHAN', 'co. Monaghan'), ('OFFALY', 'co. Offaly'), ('ROSCOMMON', 'co. Roscommon'), ('SLIGO', 'co. Sligo'), ('TIPPERARY', 'co. Tipperary'), ('WATERFORD_CITY', 'Waterford'), ('WATERFORD_COUNTY', 'co. Waterford'), ('WESTMEATH', 'co. Westmeath'), ('WEXFORD', 'co. Wexford'), ('WICKLOW', 'co. Wicklow'), ('NORTHERN_IRELAND', 'Northern Ireland'), ('UK', 'UK'), ('EUROPE', 'Europe'), ('WORDLWIDE', 'Worldwide')], max_length=50),
        ),
    ]
