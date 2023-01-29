from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    CATEGORY = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('DD', 'ДД'),
        ('sellers', 'Торговцы'),
        ('gild_masters', 'Гилдмастеры'),
        ('quest_givers', 'Квестгиверы'),
        ('smiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potion_makers', 'Зельевары'),
        ('spell_masters', 'Мастера заклинаний')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=16, choices=CATEGORY, default='tank')
    upload = models.FileField(upload_to='uploads/', default=None)


class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def accept(self):
        self.accepted = True
        self.save()
