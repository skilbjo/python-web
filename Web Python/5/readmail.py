import imaplib

mailserver = imap.IMAP_SSL('imap.gmail.com',993)

username = 'johnskilbeck'
password = 'password'
mailserver.log(username,password)

status, count = mailserver.select('Inbox')
status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')

print data[0][1]

mailserver.close()
mailserver.logout()