import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Diego Caardoza'
email['to'] = 'lietail99211@gmail.com'
email['subject'] = 'Practice'

email.set_content('I am a python student')
#smtplib.SMTP_SSL
with smtplib.SMTP_SSL('64.233.184.108',465) as smtp:
    smtp.ehlo()
    #smtp.starttls()
    smtp.login('ArkLanefgofeh@gmail.com', 'gachaplayer99211')
    smtp.send_message(email)
    print('All good boss')