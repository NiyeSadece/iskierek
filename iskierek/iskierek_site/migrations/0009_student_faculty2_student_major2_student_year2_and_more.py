# Generated by Django 4.2.13 on 2024-07-17 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("iskierek_site", "0008_student_photo_alter_student_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="faculty2",
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
            name="major2",
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
                default=None,
                max_length=3,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="year2",
            field=models.CharField(
                choices=[
                    ("1", "I rok"),
                    ("2", "II rok"),
                    ("3", "III rok"),
                    ("4", "IV rok"),
                    ("5", "V rok"),
                    ("d1", "doktorat, I rok"),
                    ("d2", "doktorat, II rok"),
                    ("d3", "doktorat, III rok"),
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
            name="living",
            field=models.CharField(
                choices=[
                    ("AP", "akademik Pyxis"),
                    ("AL", "akademik Lyra"),
                    ("AC", "akademik Crux"),
                    ("DM", "dom w Brightway"),
                    ("DR", "dom rodzinny"),
                    ("DK", "domek w Brightway"),
                    ("MM", "mieszkanie w Brightway"),
                ],
                max_length=2,
            ),
        ),
        migrations.CreateModel(
            name="Professor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=125)),
                ("last_name", models.CharField(max_length=125)),
                ("dob", models.DateField()),
                (
                    "element",
                    models.CharField(
                        choices=[
                            ("O", "ogień"),
                            ("E", "elektryczność"),
                            ("P", "powietrze"),
                            ("Z", "ziemia"),
                            ("W", "woda"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "living",
                    models.CharField(
                        choices=[
                            ("AP", "akademik Pyxis"),
                            ("AL", "akademik Lyra"),
                            ("AC", "akademik Crux"),
                            ("DM", "dom w Brightway"),
                            ("DR", "dom rodzinny"),
                            ("DK", "domek w Brightway"),
                            ("MM", "mieszkanie w Brightway"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "faculty",
                    models.CharField(
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
                        max_length=3,
                    ),
                ),
                (
                    "faculty2",
                    models.CharField(
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
                        max_length=3,
                    ),
                ),
                (
                    "year",
                    models.CharField(
                        choices=[
                            ("1", "I rok"),
                            ("2", "II rok"),
                            ("3", "III rok"),
                            ("4", "IV rok"),
                            ("5", "V rok"),
                            ("d1", "doktorat, I rok"),
                            ("d2", "doktorat, II rok"),
                            ("d3", "doktorat, III rok"),
                            ("a1", "absolwentka"),
                            ("a2", "absolwent"),
                            ("a3", "absolwencie"),
                            ("w1", "wykładowczyni"),
                            ("w2", "wykładowca"),
                            ("w3", "wykładowcze"),
                        ],
                        max_length=2,
                    ),
                ),
                ("photo", models.URLField(max_length=400, null=True)),
                (
                    "major",
                    models.CharField(
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
                            ("IAND", "iskra Andromedy"),
                            ("IAUR", "iskra Aurigi"),
                            ("ICSS", "iskra Cassiopei"),
                            ("ICAS", "iskra Castora"),
                            ("ICET", "iskra Cetusa"),
                            ("IERI", "iskra Eridanusa"),
                            ("IHYD", "iskra Hydrusa"),
                            ("ILYN", "iskra Lynx"),
                            ("IMON", "iskra Monocerosa"),
                            ("IORI", "iskra Oriona"),
                            ("IPOL", "iskra Polaris"),
                            ("ISER", "iskra Serpensa"),
                            ("ISIR", "iskra Siriusa"),
                            ("IVOL", "iskra Volansa"),
                            ("IANT", "iskra Antaresa"),
                            ("IBEL", "iskra Bellatrix"),
                            ("ICOR", "iskra Corvusa"),
                            ("IDRA", "iskra Draco"),
                            ("IOCT", "iskra Octans"),
                            ("IPLL", "iskra Polluxa"),
                            ("IUNI", "iskry unikatowe"),
                        ],
                        max_length=4,
                    ),
                ),
                (
                    "major2",
                    models.CharField(
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
                            ("IAND", "iskra Andromedy"),
                            ("IAUR", "iskra Aurigi"),
                            ("ICSS", "iskra Cassiopei"),
                            ("ICAS", "iskra Castora"),
                            ("ICET", "iskra Cetusa"),
                            ("IERI", "iskra Eridanusa"),
                            ("IHYD", "iskra Hydrusa"),
                            ("ILYN", "iskra Lynx"),
                            ("IMON", "iskra Monocerosa"),
                            ("IORI", "iskra Oriona"),
                            ("IPOL", "iskra Polaris"),
                            ("ISER", "iskra Serpensa"),
                            ("ISIR", "iskra Siriusa"),
                            ("IVOL", "iskra Volansa"),
                            ("IANT", "iskra Antaresa"),
                            ("IBEL", "iskra Bellatrix"),
                            ("ICOR", "iskra Corvusa"),
                            ("IDRA", "iskra Draco"),
                            ("IOCT", "iskra Octans"),
                            ("IPLL", "iskra Polluxa"),
                            ("IUNI", "iskry unikatowe"),
                        ],
                        max_length=4,
                    ),
                ),
                (
                    "dorm",
                    models.CharField(
                        choices=[
                            ("AP", "akademik Pyxis"),
                            ("AL", "akademik Lyra"),
                            ("AC", "akademik Crux"),
                        ],
                        max_length=2,
                    ),
                ),
                ("how_long", models.DateField()),
                ("how_long2", models.DateField()),
                (
                    "club",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="iskierek_site.club",
                    ),
                ),
                (
                    "extracurricular",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="iskierek_site.extracurricular",
                    ),
                ),
                (
                    "spark",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="iskierek_site.spark",
                    ),
                ),
                (
                    "sport",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="iskierek_site.sport",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="iskierek_site.discorduser",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
