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
    PR1 = models.ForeignKey(Player, verbose_name='左プロップ', on_delete=models.PROTECT, related_name='PR1_player')
    HO = models.ForeignKey(Player, verbose_name='フッカー', on_delete=models.PROTECT, related_name='HO_player')
    PR2 = models.ForeignKey(Player, verbose_name='右プロップ', on_delete=models.PROTECT, related_name='PR2_player')
    LO1 = models.ForeignKey(Player, verbose_name='左ロック', on_delete=models.PROTECT, related_name='LO1_player')

    def __str__(self):
        return self.name
