from django.urls import path
from . import views
from .views import PlayerDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('G_players', views.G_players, name='G_players'),
    path('DB_players', views.DB_players, name='DB_players'),
    path('T_players', views.T_players, name='T_players'),
    path('C_players', views.C_players, name='C_players'),
    path('D_players', views.D_players, name='D_players'),
    path('S_players', views.S_players, name='S_players'),
    path('L_players', views.L_players, name='L_players'),
    path('H_players', views.H_players, name='H_players'),
    path('E_players', views.E_players, name='E_players'),
    path('M_players', views.M_players, name='M_players'),
    path('F_players', views.F_players, name='F_players'),
    path('Bs_players', views.Bs_players, name='Bs_players'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('detail/<int:pk>', PlayerDetail.as_view(), name='detail'),
]
