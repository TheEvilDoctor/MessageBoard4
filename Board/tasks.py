from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from .models import *
from django.template.loader import render_to_string
from MessageBoard.MessageBoard import settings
from django.dispatch import receiver
from django.db.models.signals import m2m_changed


def send_notification_new(pk, category, title, text):
    html_content = render_to_string(
        'new_message_email.html',
        {
            'text': text,
            'link': f'{settings.SITE_URL}/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body=text,
        from_email=settings.DEFAULT_FROM_EMAIL,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=Message)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'message_add':
        author = Message.post.author.email
        send_notification_new(instance.preview(), instance.pk, instance.title, author)
