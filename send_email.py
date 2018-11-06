import smtplib
#create a smtp object with port = 587.can also use 465 
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
#identifying to server(like a hello server)
smtp_object.ehlo()
#puts the smtp connection in TLS(for encryption)
smtp_object.starttls()
#getpass is to hide the input 
import getpass
email = getpass.getpass('Email: ')
password = getpass.getpass('password: ')
#login of the gmail to send from
smtp_object.login(email,password)
to_email = getpass.getpass('Email: ')
from_address = email
to_address = to_email
subject = input("enter the subject line: ")
message = input("enter the message line: ")
#the input style is specific like this
msg = "Subject: "+subject+'\n'+message
#sends the mail
smtp_object.sendmail(from_address,to_address,msg)
#to close the connection
smtp_object.quit()