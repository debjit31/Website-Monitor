import requests
import smtplib
import time
from secrets import EMAIL_ADDRESS, EMAIL_PASSWORD
while True:
    r = requests.get('https://coreyms.com', timeout=5)

    if r.status_code != 200:
        print("Sending Email ......")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = 'TESTING EMAIL SENDING WITH PYTHON'
            body = 'I sent you an email using a python script'

            msg = f'Subject : {subject}\n\n{body}'

            smtp.sendmail(EMAIL_ADDRESS, 'ani.baner@gmail.com', msg)
            print("Email SENT!!")
    else:
        print("Site is working FINE!!")

    time.sleep(5)
