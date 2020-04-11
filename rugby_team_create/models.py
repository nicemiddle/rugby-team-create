from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField('選手名', max_length=225)
    nationality = models.CharField('代表チーム', max_length=225)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField('チーム名', max_length=225)
    creater_name = models.CharField('製作者名', max_length=225, null=True)
    PR1 = models.ForeignKey(Player, verbose_name='左プロップ', on_delete=models.PROTECT, related_name='PR1_player', null=True, blank=True)
    HO = models.ForeignKey(Player, verbose_name='フッカー', on_delete=models.PROTECT, related_name='HO_player', null=True, blank=True)
    PR2 = models.ForeignKey(Player, verbose_name='右プロップ', on_delete=models.PROTECT, related_name='PR2_player', null=True, blank=True)
    LO1 = models.ForeignKey(Player, verbose_name='左ロック', on_delete=models.PROTECT, related_name='LO1_player', null=True, blank=True)
    LO2 = models.ForeignKey(Player, verbose_name='右ロック', on_delete=models.PROTECT, related_name='LO2_player', null=True, blank=True)
    FL1 = models.ForeignKey(Player, verbose_name='左フランカー', on_delete=models.PROTECT, related_name='FL1_player', null=True, blank=True)
    FL2 = models.ForeignKey(Player, verbose_name='右フランカー', on_delete=models.PROTECT, related_name='FL2_player', null=True, blank=True)
    NO8 = models.ForeignKey(Player, verbose_name='ナンバーエイト', on_delete=models.PROTECT, related_name='NO8_player', null=True, blank=True)
    SH = models.ForeignKey(Player, verbose_name='スクラムハーフ', on_delete=models.PROTECT, related_name='SH_player', null=True, blank=True)
    SO = models.ForeignKey(Player, verbose_name='スタンドオフ', on_delete=models.PROTECT, related_name='SO_player', null=True, blank=True)
    WTB1 = models.ForeignKey(Player, verbose_name='左ウイング', on_delete=models.PROTECT, related_name='WTB1_player', null=True, blank=True)
    CTB1 = models.ForeignKey(Player, verbose_name='左センター', on_delete=models.PROTECT, related_name='CTB1_player', null=True, blank=True)
    CTB2 = models.ForeignKey(Player, verbose_name='右センター', on_delete=models.PROTECT, related_name='CTB2_player', null=True, blank=True)
    WTB2 = models.ForeignKey(Player, verbose_name='右ウイング', on_delete=models.PROTECT, related_name='WTB2_player', null=True, blank=True)
    FB = models.ForeignKey(Player, verbose_name='フルバック', on_delete=models.PROTECT, related_name='FB_player', null=True, blank=True)

    def __str__(self):
        return self.name
