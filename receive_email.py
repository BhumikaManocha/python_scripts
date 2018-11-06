import imaplib
#protocol for secure connection wih the server
m = imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
email = getpass.getpass("email :")
#password is the app password here that you generate from 2 step verification
password = getpass.getpass("password :")
m.login(email,password)
m.list()
#slecting what you want from the list
m.select('inbox')
typ, data = m.search(None,'FROM smaple_email@gmail.com')
for num in data[0].split():
    typ, data = m.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
   
m.close()
m.logout()