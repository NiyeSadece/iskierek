from django.contrib import admin
from .models import DiscordUser, Spark, Club, Sport, Extracurricular, Student, Professor


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

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass