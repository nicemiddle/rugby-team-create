# Generated by Django 3.0.4 on 2020-04-11 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rugby_team_create', '0002_team_creater_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='CTB1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='CTB1_player', to='rugby_team_create.Player', verbose_name='左センター'),
        ),
        migrations.AddField(
            model_name='team',
            name='CTB2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='CTB2_player', to='rugby_team_create.Player', verbose_name='右センター'),
        ),
        migrations.AddField(
            model_name='team',
            name='FB',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='FB_player', to='rugby_team_create.Player', verbose_name='フルバック'),
        ),
        migrations.AddField(
            model_name='team',
            name='FL1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='FL1_player', to='rugby_team_create.Player', verbose_name='左フランカー'),
        ),
        migrations.AddField(
            model_name='team',
            name='FL2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='FL2_player', to='rugby_team_create.Player', verbose_name='右フランカー'),
        ),
        migrations.AddField(
            model_name='team',
            name='LO2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='LO2_player', to='rugby_team_create.Player', verbose_name='右ロック'),
        ),
        migrations.AddField(
            model_name='team',
            name='NO8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='NO8_player', to='rugby_team_create.Player', verbose_name='ナンバーエイト'),
        ),
        migrations.AddField(
            model_name='team',
            name='SH',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SH_player', to='rugby_team_create.Player', verbose_name='スクラムハーフ'),
        ),
        migrations.AddField(
            model_name='team',
            name='SO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SO_player', to='rugby_team_create.Player', verbose_name='スタンドオフ'),
        ),
        migrations.AddField(
            model_name='team',
            name='WTB1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='WTB1_player', to='rugby_team_create.Player', verbose_name='左ウイング'),
        ),
        migrations.AddField(
            model_name='team',
            name='WTB2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='WTB2_player', to='rugby_team_create.Player', verbose_name='右ウイング'),
        ),
        migrations.AlterField(
            model_name='team',
            name='HO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='HO_player', to='rugby_team_create.Player', verbose_name='フッカー'),
        ),
        migrations.AlterField(
            model_name='team',
            name='LO1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='LO1_player', to='rugby_team_create.Player', verbose_name='左ロック'),
        ),
        migrations.AlterField(
            model_name='team',
            name='PR1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='PR1_player', to='rugby_team_create.Player', verbose_name='左プロップ'),
        ),
        migrations.AlterField(
            model_name='team',
            name='PR2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='PR2_player', to='rugby_team_create.Player', verbose_name='右プロップ'),
        ),
    ]
