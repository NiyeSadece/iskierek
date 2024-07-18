from django.db import models
import datetime


class DiscordUser(models.Model):
    name = models.CharField(max_length=125)
    discord_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    exp = models.IntegerField(default=0)
    lvl = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Spark (models.Model):
    NAME = [
        ("AND", "Andromedy"),
        ("AUR", "Aurigi"),
        ("CSS", "Cassiopei"),
        ("CAS", "Castora"),
        ("CET", "Cetusa"),
        ("ERI", "Eridanusa"),
        ("HYD", "Hydrusa"),
        ("LYN", "Lynx"),
        ("MON", "Monocerosa"),
        ("ORI", "Oriona"),
        ("POL", "Polaris"),
        ("SER", "Serpensa"),
        ("SIR", "Siriusa"),
        ("VOL", "Volansa"),
        ("ANT", "Antaresa"),
        ("BEL", "Bellatrix"),
        ("COR", "Corvusa"),
        ("DRA", "Draco"),
        ("OCT", "Octans"),
        ("PLL", "Polluxa"),
        ]

    RARITY =[
        (1, "powszechna"),
        (2, "rzadka"),
        (3, "unikatowa"),
        ]
    name = models.CharField(max_length=3, choices=NAME)
    rarity = models.IntegerField(choices=RARITY)

    def get_name_display(self):
        return dict(self.NAME).get(self.name)

    def get_rarity_display(self):
        return dict(self.RARITY).get(self.rarity)

    def __str__(self):
        return self.get_name_display()


class Extracurricular(models.Model):
    NAME = [
        ("chór", "chór uniwersytecki"),
        ("gazetka", "gazeta \"Głos Młodego Miasta\""),
        ("moda", "koło modowe"),
        ("gospodynie", "koło praktycznych umiejętności"),
        ("teatr", "koło teatralne"),
        ("wolontariat", "wolontariat"),
        ]

    SPECIAL = [
        ("p1", "przewodnicząca"),
        ("p2", "przewodniczący"),
        ("p3", "przewodniczące"),
        ("o1", "opiekunka"),
        ("o2", "opiekun"),
        ("o3", "opiekuńcze"),
        ]

    name = models.CharField(max_length=11, choices=NAME)
    special = models.CharField(max_length=2, choices=SPECIAL, blank=True)

    def get_name_display(self):
        return dict(self.NAME).get(self.name)

    def get_special_display(self):
        return dict(self.SPECIAL).get(self.special)

    def __str__(self):
        if self.get_special_display():
            return f"{self.get_name_display()}, {self.get_special_display()}"
        else:
            return self.get_name_display()


class Club (models.Model):
    NAME = [
        ("książka", "literacki"),
        ("dyskusja", "dyskusyjny"),
        ("sport", "sportów rekreacyjnych"),
        ("zwierzę", "miłośników zwierząt"),
        ("astrologia", "astrologiczny"),
        ("robot", "robotyczny"),
        ("wycieczka", "wycieczkowo-survivalowy"),
        ("film", "filmowy"),
        ("zielę", "zielników"),
        ("gra", "miłośnicy gier"),
        ]

    SPECIAL = [
        ("p1", "przewodnicząca"),
        ("p2", "przewodniczący"),
        ("p3", "przewodniczące"),
        ("o1", "opiekunka"),
        ("o2", "opiekun"),
        ("o3", "opiekuńcze"),
        ]

    name = models.CharField(max_length=15, choices=NAME)
    special = models.CharField(max_length=2, choices=SPECIAL, blank=True)

    def get_name_display(self):
        return dict(self.NAME).get(self.name)

    def get_special_display(self):
        return dict(self.SPECIAL).get(self.special)

    def __str__(self):
        if self.get_special_display():
            return f"{self.get_name_display()}, {self.get_special_display()}"
        else:
            return self.get_name_display()


class Sport(models.Model):
    NAME = [
        ("łuk", "łucznictwo"),
        ("hojek", "hokej"),
        ("basen", "basen"),
        ("siatka", "siatkówka"),
        ("kosz", "koszykówka"),
        ("boks", "boks"),
        ("taniec", "taniec"),
        ]

    SPECIAL = [
        ("p1", "kapitan"),
        ("p2", "kapitanka"),
        ("p3", "kapitańcze"),
        ("o1", "trenerka"),
        ("o2", "trener"),
        ("o3", "trenerze"),
        ]

    name = models.CharField(max_length=15, choices=NAME)
    special = models.CharField(max_length=2, choices=SPECIAL, blank=True)

    def get_name_display(self):
        return dict(self.NAME).get(self.name)

    def get_special_display(self):
        return dict(self.SPECIAL).get(self.special)

    def __str__(self):
        if self.get_special_display():
            return f"{self.get_name_display()}, {self.get_special_display()}"
        else:
            return self.get_name_display()

class Person (models.Model):
    ELEMENT = [
        ("O", "ogień"),
        ("E", "elektryczność"),
        ("P", "powietrze"),
        ("Z", "ziemia"),
        ("W", "woda"),
        ]
    LIVING = [
        ("AP", "akademik Pyxis"),
        ("AL", "akademik Lyra"),
        ("AC", "akademik Crux"),
        ("DM", "dom w Brightway"),
        ("DR", "dom rodzinny"),
        ("DK", "domek w Brightway"),
        ("MM", "mieszkanie w Brightway"),
        ]
    FACULTY = [
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
        ]
    YEAR = [
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
        ]
    MAJOR = [
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
        ]

    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    dob = models.DateField()
    element = models.CharField(max_length=1, choices=ELEMENT)
    spark = models.ForeignKey(Spark, on_delete=models.CASCADE)
    living = models.CharField(max_length=2, choices=LIVING)
    extracurricular = models.ForeignKey(Extracurricular, on_delete=models.CASCADE, blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, blank=True, null=True)
    major = models.CharField(max_length=3, choices=MAJOR)
    major2 = models.CharField(max_length=3, choices=MAJOR, blank=True, null=True)
    faculty = models.CharField(max_length=3, choices=FACULTY)
    faculty2 = models.CharField(max_length=3, choices=FACULTY, blank=True, null=True)
    year = models.CharField(max_length=2, choices=YEAR)
    photo = models.URLField(max_length=400, null=True)

    def age(self):
        today = datetime.datetime.now().date()
        return today.year + 70 - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    class Meta:
        abstract = True

class Student (Person):
    year2 = models.CharField(max_length=2, choices=Person.YEAR, blank=True, null=True)
    def __str__(self):
        return self.name + " " + self.last_name

class Professor(Person):
    TEACHING = Person.MAJOR + [
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
        ]
    DORM = [
        ("AP", "akademik Pyxis"),
        ("AL", "akademik Lyra"),
        ("AC", "akademik Crux"),
        ]
    DORM_SPECIAL = [
        ("z1", "zarządczyni"),
        ("z2", "zarządca"),
        ("z3", "zarządcze"),
        ]
    major = models.CharField(max_length=4, choices=TEACHING)
    major2 = models.CharField(max_length=4, choices=TEACHING, blank=True, null=True)
    dorm = models.CharField(max_length=2, choices=DORM, blank=True, null=True)
    dorm_special = models.CharField(max_length=2, choices=DORM_SPECIAL, blank=True, null=True)
    how_long = models.DateField()
    how_long2 = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.name + " " + self.last_name

    def teaching_duration(self, how_long):
        today = datetime.datetime.now().date()
        start_date = how_long

        years = today.year - start_date.year + 70
        months = today.month - start_date.month

        if months < 0:
            years -= 1
            months += 12

        half_years = 0

        if start_date.month <= 3:
            half_years += 1
        if start_date.month <= 9:
            half_years += 1

        if today.month >= 9:
            half_years += 1
        elif today.month >= 3:
            half_years += 1

        total_half_years = years * 2 + half_years

        return total_half_years / 2

    def teaching(self):
        duration = self.teaching_duration(self.how_long)
        years = int(duration)
        half_years = (duration - years) * 2
        for_grammar = str(years)

        if for_grammar[-1] == 2 or for_grammar[-1] == 3 or for_grammar[-1] == 4:
            for_grammar = "lata"
        else:
            for_grammar = "lat"

        if half_years == 1:
            return f"{years} {for_grammar} i pół roku"
        else:
            return f"{years} {for_grammar}"

    def teaching2(self):
        duration = self.teaching_duration(self.how_long2)
        years = int(duration)
        half_years = (duration - years) * 2
        for_grammar = str(years)

        if for_grammar[-1] == 2 or for_grammar[-1] == 3 or for_grammar[-1] == 4:
            for_grammar = "lata"
        else:
            for_grammar = "lat"

        if half_years == 1:
            return f"{years} {for_grammar} i pół roku"
        else:
            return f"{years} {for_grammar}"