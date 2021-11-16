from django.db import models


class Ticket(models.Model):
    author = models.ForeignKey(
        'auth.User', 
        related_name='tickets', 
        on_delete=models.CASCADE
        )
    created = models.DateTimeField(
        auto_now_add=True
        )
    title = models.CharField(
        max_length=50, 
        blank=True, 
        default=''
        )
    text = models.TextField(
        blank=True, 
        default=''
        )

    class Meta:
        ordering = ['created']

class Comment(models.Model):
    author = models.ForeignKey(
        'auth.User',
        related_name='comments', 
        on_delete=models.CASCADE
        )
    created = models.DateTimeField(
        auto_now_add=True
        )
    text = models.TextField(
        blank=False
        )
    ticket = models.ForeignKey(
        'Ticket', 
        related_name='comments', 
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ['created']