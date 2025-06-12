from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.timezone import now



def send_email_for_confirmation(user_email: str, token: str):
    confirmation_url = f"{settings.BASE_URL}/confirm_email/{token}/"
    message = render_to_string('emails/confirmation_email.html', {
        'confirmation_url': confirmation_url,
        'year': now().year,
    })

    email = EmailMessage(
        subject="Confirmez votre adresse e-mail",
        body=message,
        to=[user_email],
    )
    email.content_subtype = "html"  # IMPORTANT pour que ce soit interprété en HTML
    email.send()