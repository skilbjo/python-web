import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = 'skilbjo@gmail.com'
toaddr = 'john.skilbeck@gmail'
text = 'test message sent from Python'
username = 'skilbjo'
password = 'password'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.gmail.com:58')
server.ehlo()
server.startttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()