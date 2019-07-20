from django.contrib import admin

from .models import IA, Stats, PawnsType, Pawns, Game

admin.site.register(IA)
admin.site.register(Stats)
admin.site.register(PawnsType)
admin.site.register(Pawns)
admin.site.register(Game)
