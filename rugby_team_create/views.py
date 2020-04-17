from django.shortcuts import render
from django.views import generic
from .models import Team, Player
from .forms import TeamCreateForm, PlayerCreateForm
from django.urls import reverse_lazy

# Create your views here.
class TopTemplate(generic.TemplateView):
    template_name = 'rugby_team_create/top.html'

class TeamList(generic.ListView):
    model = Team

class TeamDetail(generic.DetailView):
    model = Team

class TeamCreate(generic.CreateView):
    model = Team
    success_url = reverse_lazy('rugby_team_create:team_list')
    form_class = TeamCreateForm

#チームの削除
class TeamDelete(generic.DeleteView):
    model = Team
    success_url = reverse_lazy('rugby_team_create:team_list')

#選手一覧表示
class PlayerList(generic.ListView):
    model = Player

#選手登録（入力フォーム、登録後選手一覧ページへ）
class PlayerCreate(generic.CreateView):
    model = Player
    success_url = reverse_lazy('rugby_team_create:player_list')
    form_class = PlayerCreateForm
