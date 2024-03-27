from django.db import models

class Bets(models.Model):
    amount = models.IntegerField()
    STATUS_CHOICES = [
        ('PENDING', 'Ещё не сыграла'),
        ('WON', 'Выиграла'),
        ('LOST', 'Проиграла')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Bet'
        verbose_name_plural = 'Bets'
