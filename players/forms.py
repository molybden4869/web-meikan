from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['team', 'name', 'uniform_number', 'position', 'birthday',
            'height', 'weight', 'pitch_and_bat', 'draft_round',
            'professional_years', 'cheering_song', 'coment']

        