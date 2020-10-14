from django.contrib import admin
from .models import Team, Position, Pitch_and_Bat, Draft_round, Player

admin.site.register(Team)
admin.site.register(Position)
admin.site.register(Pitch_and_Bat)
admin.site.register(Draft_round)
admin.site.register(Player)

