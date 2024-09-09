# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# host_address = "umeshpolavarapu71@gmail.com"
# host_pass = "mypass"
# guest_address = "guest@gmail.com"
# subject = "Report "
# content = '''Test failed restart services'''

# message = MIMEMultipart()
# message['From'] = host_address
# message['To'] = guest_address
# message['Subject'] = subject
# message.attach(MIMEText(content, 'plain'))

# session = smtplib.SMTP('smtp.gmail.com', 587)
# session.starttls()
# session.login(host_address, host_pass)
# text = message.as_string()
# session.sendmail(host_address, guest_address  , text)
# session.quit()

# print('Successfully sent your mail')

import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'umeshpolavarapu71@.com'
    msg['To'] = 'recipient_polavarapuumesh@gmail.com'
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('umeshpolavarapu71@gmail.com', 'Umesh@199999')
    server.sendmail('your_email@example.com', 'recipient_email@example.com', msg.as_string())
    server.quit()
if __name__ == '__main__':
    send_email('Test Email', 'This is a test email sent from Python.')