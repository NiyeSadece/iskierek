from django.db import models


class DiscordUser(models.Model):
    name = models.CharField(max_length=125)
    discord_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    exp = models.IntegerField(default=0)
    lvl = models.IntegerField(default=0)

    def __str__(self):
        return self.name
