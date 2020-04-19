from django import forms
from .models import Team, Player

class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        '''widgets = {
            'PR1':forms.Select(attrs={'class': 'PR1_form'}),
            'HO':forms.Select(attrs={'class': 'HO_form'}),
            'PR2':forms.Select(attrs={'class': 'PR2_form'}),
            'LO1':forms.Select(attrs={'class': 'LO1_form'}),
            'LO"':forms.Select(attrs={'class': 'LO2_form'}),
            'FL1':forms.Select(attrs={'class': 'FL1_form'}),
            'FL2':forms.Select(attrs={'class': 'FL2_form'}),
            'NO8':forms.Select(attrs={'class': 'NO8_form'}),
            'SH':forms.Select(attrs={'class': 'SH_form'}),
            'SO':forms.Select(attrs={'class': 'SO_form'}),
            'WTB1':forms.Select(attrs={'class': 'WTB1_form'}),
            'CTB1':forms.Select(attrs={'class': 'CTB1_form'}),
            'CTB2':forms.Select(attrs={'class': 'CTB2_form'}),
            'WTB2':forms.Select(attrs={'class': 'WTB2_form'}),
            'FB':forms.Select(attrs={'class': 'FB_form'}),
        }'''


class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
