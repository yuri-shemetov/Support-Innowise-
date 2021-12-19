from django.core.mail import send_mail

def send(user_mail):
    send_mail(
        'Вы подписались на рассылку',
        'Вот ваше новое сообщение',
        'yuri7shemetov@gmail.com',
        [user_mail],
        fail_silently=False,
    )