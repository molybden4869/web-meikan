from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import DetailView
from .models import Player
from .forms import PlayerForm


# Home画面
def index(request):
    params = {
        'title': 'プロ野球Web選手名鑑',
    }

    return render(request, 'players/index.html', params)


# ジャイアンツの選手リスト
def G_players(request):
    data = Player.objects.filter(team__team='巨人')
    params = {
        'title': 'ジャイアンツ選手名鑑',
        'data': data,
    }

    return render(request, 'players/G_players.html', params)


# ベイスターズの選手リスト
def DB_players(request):
    data = Player.objects.filter(team__team='DeNA')
    params = {
        'title': 'ベイスターズ選手名鑑',
        'data': data,
    }

    return render(request, 'players/DB_players.html', params)


# タイガースの選手リスト
def T_players(request):
    data = Player.objects.filter(team__team='阪神')
    params = {
        'title': 'タイガース選手名鑑',
        'data': data,
    }

    return render(request, 'players/T_players.html', params)


# カープの選手リスト
def C_players(request):
    data = Player.objects.filter(team__team='広島')
    params = {
        'title': 'カープ選手名鑑',
        'data': data,
    }

    return render(request, 'players/C_players.html', params)


# ドラゴンズの選手リスト
def D_players(request):
    data = Player.objects.filter(team__team='中日')
    params = {
        'title': 'ドラゴンズ選手名鑑',
        'data': data,
    }

    return render(request, 'players/D_players.html', params)


# スワローズの選手リスト
def S_players(request):
    data = Player.objects.filter(team__team='ヤクルト')
    params = {
        'title': 'スワローズ選手名鑑',
        'data': data,
    }

    return render(request, 'players/S_players.html', params)


# ライオンズの選手リスト
def L_players(request):
    data = Player.objects.filter(team__team='西武')
    params = {
        'title': 'ライオンズ選手名鑑',
        'data': data,
    }

    return render(request, 'players/L_players.html', params)


# ホークスの選手リスト
def H_players(request):
    data = Player.objects.filter(team__team='ソフトバンク')
    params = {
        'title': 'ホークス選手名鑑',
        'data': data,
    }

    return render(request, 'players/H_players.html', params)


# イーグルスの選手リスト
def E_players(request):
    data = Player.objects.filter(team__team='楽天')
    params = {
        'title': 'イーグルス選手名鑑',
        'data': data,
    }

    return render(request, 'players/E_players.html', params)


# マリーンズの選手リスト
def M_players(request):
    data = Player.objects.filter(team__team='ロッテ')
    params = {
        'title': 'マリーンズ選手名鑑',
        'data': data,
    }

    return render(request, 'players/M_players.html', params)


# ファイターズの選手リスト
def F_players(request):
    data = Player.objects.filter(team__team='日本ハム')
    params = {
        'title': 'ファイターズ選手名鑑',
        'data': data,
    }

    return render(request, 'players/F_players.html', params)


# バファローズの選手リスト
def Bs_players(request):
    data = Player.objects.filter(team__team='オリックス')
    params = {
        'title': 'バファローズ選手名鑑',
        'data': data,
    }

    return render(request, 'players/Bs_players.html', params)


# 選手の登録
def create(request):
    params = {
        'title': '選手の登録',
        'message': '各項目を入力すると選手の登録ができます　登録が完了するとHomeに戻ります',
        'form': PlayerForm(),
    }
    if (request.method == 'POST'):
            instance = Player()
            form = PlayerForm(request.POST, instance=instance)
            params['form'] = form
            if (form.is_valid()):
                form.save()
                return redirect(to='/players')
            else:
                params['message'] = '登録できません 各項目の値を確認してください'
    
    return render(request, 'players/create.html', params)


# 選手情報の編集
def edit(request, num):
    instance = Player.objects.get(id=num)
    params = {
        'title': '選手情報の編集',
        'id': num,
        'form': PlayerForm(instance=instance),
    }
    
    if (request.method == 'POST'):
        form = PlayerForm(request.POST, instance=instance)
        params['form'] = form
        if (form.is_valid()):
            form.save()
            return redirect(to='/players')
        
    return render(request, 'players/edit.html', params)


# 選手情報の削除
def delete(request, num):
    player = Player.objects.get(id=num)
    if (request.method == 'POST'):
        player.delete()
        return redirect(to='/players')
    
    params = {
        'title': '選手の削除',
        'id': num,
        'player': player,
    }
    
    return render(request, 'players/delete.html', params)


# 選手情報の詳細
class PlayerDetail(DetailView):
    model = Player


  






