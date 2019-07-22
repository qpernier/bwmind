from django.contrib import admin

from .models import IA, Stat, PawnsType, Pawn, Game

admin.site.register(IA)
admin.site.register(Stat)
admin.site.register(PawnsType)
admin.site.register(Pawn)
admin.site.register(Game)
