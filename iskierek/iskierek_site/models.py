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
        return f"{self.get_name_display()}, {self.get_special_display()}"


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
        return f"{self.get_name_display()}, {self.get_special_display()}"


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
        return f"{self.get_name_display()}, {self.get_special_display()}"


class Major (models.Model):
    NAME = [
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
        ]

    name = models.CharField(max_length=3, choices=NAME)
    faculty = models.CharField(max_length=3, choices=FACULTY)
    year = models.CharField(max_length=2, choices=YEAR)

    def get_name_display(self):
        return dict(self.NAME).get(self.name)

    def get_faculty_display(self):
        return dict(self.FACULTY).get(self.faculty)

    def get_year_display(self):
        return dict(self.YEAR).get(self.year)

    def __str__(self):
        return f"{self.get_name_display()}, {self.get_year_display()}"

class Student (models.Model):
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
        ("MM", "mieszkanie w Brightway"),
        ]

    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    dob = models.DateField()
    element = models.CharField(max_length=1, choices=ELEMENT)
    spark = models.ForeignKey(Spark, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=True)
    extracurricular = models.ForeignKey(Extracurricular, on_delete=models.CASCADE, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, blank=True)
    living = models.CharField(max_length=2, choices=LIVING)

    def __str__(self):
        return self.name

    def age(self):
        return datetime.now().year + 70 - self.dob.year