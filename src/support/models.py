from django.db import models

class Status(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="status"
    )
    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name="Status"
        verbose_name_plural="Statuses"

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
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name='ticket_status',
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
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name='answer_status',
        )

    class Meta:
        ordering = ['created']