from django.db import models
from django.core.validators import RegexValidator, MinValueValidator


# チームのクラス
class Team(models.Model):
    team_choices = [
        ('巨人', '巨人'),
        ('DeNA', 'DeNA'),
        ('阪神', '阪神'),
        ('広島', '広島'),
        ('中日', '中日'),
        ('ヤクルト', 'ヤクルト'),
        ('西武', '西武'),
        ('ソフトバンク', 'ソフトバンク'),
        ('楽天', '楽天'),
        ('ロッテ', 'ロッテ'),
        ('日本ハム', '日本ハム'),
        ('オリックス', 'オリックス'),
    ]
    team = models.CharField(max_length=6, choices=team_choices)

    def __str__(self):
        return self.team


# 守備位置のクラス
class Position(models.Model):
    position_choices = [
        ('投手', '投手'),
        ('捕手', '捕手'),
        ('内野手', '内野手'),
        ('外野手', '外野手'),
    ]
    position = models.CharField(max_length=3, choices=position_choices)
    
    def __str__(self):
        return self.position


# 投打のクラス
class Pitch_and_Bat(models.Model):
    pb_choices = [
        ('右投げ右打ち', '右投げ右打ち'),
        ('右投げ左打ち', '右投げ左打ち'),
        ('右投げ両打ち', '右投げ両打ち'),
        ('左投げ右打ち', '左投げ右打ち'),
        ('左投げ左打ち', '左投げ左打ち'),
        ('左投げ両打ち', '左投げ両打ち'),
    ]
    pitch_and_bad = models.CharField(max_length=6, choices=pb_choices)
    
    def __str__(self):
        return self.pitch_and_bad


# ドラフト順位のクラス
class Draft_round(models.Model):
    draft_choices = [
        ('-', '-'),
        ('１位', '１位'),
        ('２位', '２位'),
        ('３位', '３位'),
        ('４位', '４位'),
        ('５位', '５位'),
        ('６位', '６位'),
        ('７位', '７位'),
        ('８位', '８位'),
        ('９位', '９位'),
        ('育成１位', '育成１位'),
        ('育成２位', '育成２位'),
        ('育成３位', '育成３位'),
        ('育成４位', '育成４位'),
        ('育成５位', '育成５位'),
        ('育成６位', '育成６位'),
        ('育成７位', '育成７位'),
        ('育成８位', '育成８位'),
        ('育成９位', '育成９位'),
    ]
    draft_round = models.CharField(max_length=4, choices=draft_choices)

    def __str__(self):
        return self.draft_round


# 選手情報のクラス
class Player(models.Model):
    team = models.ForeignKey(Team,
        on_delete=models.CASCADE, verbose_name="チーム")   
    name = models.CharField(max_length=50, verbose_name="選手名")
    uniform_number = models.CharField(max_length=3,
        validators=[RegexValidator(r'^[0-9]*$', '数字のみです')], verbose_name="背番号")
    position = models.ForeignKey(Position,
        on_delete=models.CASCADE, verbose_name="守備位置")   
    birthday = models.DateField(verbose_name="生年月日")
    height = models.IntegerField(default=170,
        validators=[MinValueValidator(160)], verbose_name="身長")
    weight = models.IntegerField(default=70, verbose_name="体重")
    pitch_and_bat = models.ForeignKey(Pitch_and_Bat,
        on_delete=models.CASCADE, verbose_name="投打")   
    draft_round = models.ForeignKey(Draft_round,
        on_delete=models.CASCADE, verbose_name="ドラフト順位")
    professional_years = models.IntegerField(default=1,
        validators=[MinValueValidator(1)], verbose_name="プロ通算年数")
    cheering_song = models.TextField(max_length=80,
        blank=True, verbose_name="選手応援歌")
    coment = models.TextField(max_length=100,
        blank=True, verbose_name="選手紹介")

    def __str__(self):
        return  '<Player:id =' + str(self.id) + ', ' +  \
            self.name + '(' + str(self.uniform_number) + ')>'
