import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['From'] = 'Heinrich Ohwer'
email['To'] = '18022020@mahasiswa.itb.ac.id'
email['Subject'] = 'You won money click link here>>>'

email.set_content('hello...')

with smtplib.SMTP(host='smtp.office365.com',port=995) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('18022020@mahasiswa.itb.ac.id', 'hello')
    smtp.send_message(email)
    print('all good')