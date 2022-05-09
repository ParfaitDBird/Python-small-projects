import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Diego Caardoza'
email['to'] = 'ArkLanefgofeh@gmail.com'
email['subject'] = 'Practice'

email.set_content(html.substitute({'name': 'Ocelot'}), 'html')
#smtplib.SMTP_SSL
with smtplib.SMTP_SSL('64.233.184.108',465) as smtp:
    smtp.ehlo()
    #smtp.starttls()
    smtp.login('ArkLanefgofeh@gmail.com', 'gachaplayer99211')
    smtp.send_message(email)
    print('All good boss')