from django.urls import path
from . import views

app_name = 'rugby_team_create'

urlpatterns = [
    path('top/', views.TopTemplate.as_view(), name='top'),
    path('team_list/', views.TeamList.as_view(), name='team_list'),
    path('team_detail/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),
    path('team_create/', views.TeamCreate.as_view(), name='team_create'),
    path('player_list/', views.PlayerList.as_view(), name='player_list'),
    path('player_create/', views.PlayerCreate.as_view(), name='player_create'),
    path('team_delete_confirm/<int:pk>', views.TeamDelete.as_view(), name='team_delete_confirm')
]
