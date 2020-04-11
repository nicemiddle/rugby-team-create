from django import forms
from .models import Team, Player

class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
