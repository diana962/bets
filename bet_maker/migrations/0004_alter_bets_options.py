# Generated by Django 5.0.3 on 2024-03-27 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet_maker', '0003_bets_delete_bet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bets',
            options={'verbose_name': 'Bet', 'verbose_name_plural': 'Bets'},
        ),
    ]
