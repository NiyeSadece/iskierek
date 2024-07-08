from django.contrib import admin
from .models import DiscordUser


@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'discord_id',
        'is_active',
        'exp',
        'lvl',
    ]
