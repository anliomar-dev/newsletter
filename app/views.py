from django.shortcuts import render
from django.core.signing import TimestampSigner, BadSignature

from .models import Newsletter
from .utils import send_email_for_confirmation

signer = TimestampSigner()

def index(request):
    return render(request, 'app/submit_email.html')


def send_confirmation_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            token = signer.sign(email)
            send_email_for_confirmation(email, token)
            return render(request, 'app/submit_email.html', {
                'message': "We've sent your an email, Please check your inbox"
            })
        else:
            return render(request, 'app/submit_email.html', {
                'error': "Please provide a valid email"
            })
    return render(request, 'app/submit_email.html')


def confirm_email(request, token: str):
    try:
        email = signer.unsign(token)
        new_subscribe = Newsletter.objects.create(email=email)
        new_subscribe.save()
        message = f"Email address '{email}' successfully confirmed. You'll be notified at launch! 🎉"
        verified = True
    except BadSignature:
        message = "The confirmation link is invalid or has expired."
        verified = False

    return render(request, 'app/confirm_email.html', {'message': message, 'verified': verified})

