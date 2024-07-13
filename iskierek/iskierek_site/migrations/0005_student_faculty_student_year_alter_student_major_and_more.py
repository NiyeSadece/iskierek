# Generated by Django 4.2.13 on 2024-07-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iskierek_site", "0004_student_major"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="faculty",
            field=models.CharField(
                choices=[
                    ("e-b", "Ekonomiczno-Biznesowy"),
                    ("med", "Medyczny"),
                    ("hum", "Humanistyczny"),
                    ("tec", "Techniczny"),
                    ("ści", "Nauk Ścisłych"),
                    ("prz", "Przyrodniczy"),
                    ("art", "Artystyczny"),
                    ("pia", "Prawa i Administracji"),
                    ("nsp", "Nauk Społecznych"),
                    ("isk", "Iskier"),
                ],
                default=None,
                max_length=3,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="year",
            field=models.CharField(
                choices=[
                    ("1", "I"),
                    ("2", "II"),
                    ("3", "III"),
                    ("4", "IV"),
                    ("5", "V"),
                    ("d1", "doktorat, I"),
                    ("d2", "doktorat, II"),
                    ("d3", "doktorat, III"),
                    ("a1", "absolwentka"),
                    ("a2", "absolwent"),
                    ("a3", "absolwencie"),
                    ("w1", "wykładowczyni"),
                    ("w2", "wykładowca"),
                    ("w3", "wykładowcze"),
                ],
                default=None,
                max_length=2,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="student",
            name="major",
            field=models.CharField(
                choices=[
                    ("eko", "ekonomia"),
                    ("log", "logistyka"),
                    ("rif", "rachunkowość i finanse"),
                    ("zar", "zarządzanie"),
                    ("his", "historia"),
                    ("tur", "turystyka"),
                    ("lin", "lingwistyka"),
                    ("arc", "archeologia"),
                    ("pie", "pielęgniarstwo"),
                    ("dif", "dietetyka i fizjoterapia"),
                    ("kos", "kosmetologia"),
                    ("rat", "ratownictwo medyczne"),
                    ("air", "automatyka i robotyka"),
                    ("now", "nowe technologie"),
                    ("ach", "architektura"),
                    ("mat", "materiałoznawstwo"),
                    ("aif", "astronomia i fizyka"),
                    ("inf", "informatyka"),
                    ("mtm", "matematyka"),
                    ("che", "chemia"),
                    ("zie", "zielone technologia"),
                    ("geo", "geodezja"),
                    ("wet", "weterynaria"),
                    ("bio", "biologia"),
                    ("akt", "aktorstwo"),
                    ("tec", "techniki artystyczne"),
                    ("muz", "muzyka"),
                    ("tiu", "tkaniny i ubiór"),
                    ("pra", "prawo"),
                    ("kry", "kryminologia"),
                    ("oiw", "obrona i wojskowość"),
                    ("adm", "administracja"),
                    ("ped", "pedagogika"),
                    ("psy", "psychologia"),
                    ("soc", "socjologia"),
                    ("pol", "politologia"),
                    ("niż", "nauka o iskrach i żywiołach"),
                    ("gen", "genetyka uiskrzonych"),
                ],
                max_length=3,
            ),
        ),
        migrations.DeleteModel(
            name="Major",
        ),
    ]
