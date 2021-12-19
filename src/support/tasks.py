from django.core.mail import send_mail
from proj.celery import app
from .service import send
from .models import Contact

@app.task
def send_letter_email(user_email):
    send(user_email)

@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать это сообщение каждые 2 минуты',
            'yuri7shemetov@gmail.com',
            [contact.email],
            fail_silently=False
        )