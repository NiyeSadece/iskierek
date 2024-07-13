from django.contrib import admin
from .models import DiscordUser, Spark, Club, Sport, Major, Extracurricular, Student


@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'discord_id',
        'is_active',
        'exp',
        'lvl',
    ]

@admin.register(Spark)
class SparkAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'get_rarity_display')

    def get_name_display(self, obj):
        return obj.get_name_display()
    get_name_display.short_description = 'Name'

    def get_rarity_display(self, obj):
        return obj.get_rarity_display()
    get_rarity_display.short_description = 'Rarity'

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'get_special_display')

    def get_name_display(self, obj):
        return obj.get_name_display()
    get_name_display.short_description = 'Name'

    def get_special_display(self, obj):
        return obj.get_special_display()
    get_special_display.short_description = 'Special'

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'get_special_display')

    def get_name_display(self, obj):
        return obj.get_name_display()
    get_name_display.short_description = 'Name'

    def get_special_display(self, obj):
        return obj.get_special_display()
    get_special_display.short_description = 'Special'

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'get_faculty_display', 'get_year_display')

    def get_name_display(self, obj):
        return obj.get_name_display()
    get_name_display.short_description = 'Name'

    def get_faculty_display(self, obj):
        return obj.get_faculty_display()
    get_faculty_display.short_description = 'Faculty'

    def get_year_display(self, obj):
        return obj.get_year_display()
    get_year_display.short_description = 'Year'

@admin.register(Extracurricular)
class ExtracurricularAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'get_special_display')

    def get_name_display(self, obj):
        return obj.get_name_display()
    get_name_display.short_description = 'Name'

    def get_special_display(self, obj):
        return obj.get_special_display()
    get_special_display.short_description = 'Special'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass