import random
from django.core.mail import EmailMessage
from .models import customUser,OneTimePassword
from django.conf import settings


def generateOTP():
    otp = ""
    for  i in range(6):
        otp += str(random.randint(1,9))
    return otp

def send_code_to_user(email):
    subject = "One Time  Password for email Verification"
    otp_code = generateOTP()
    user = customUser.creation.get(email=email)
    current_site = "myAuth.com"
    email_body = f"hii {user.first_name} thanks for signing up on {current_site} please verify your email. Your OTP is {otp_code}"
    from_email = settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)
    send_email = EmailMessage(subject=subject,body=email_body,from_email=from_email,to=[email])
    send_email.send(fail_silently=True)