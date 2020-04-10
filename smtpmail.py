# send_attachment.py
# import necessary packages

import datetime
now = datetime.datetime.now()

print ()
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import os


def mails():
# create message object instance
 msg = MIMEMultipart()
 
 
# create message object instance

 
 
 message = "intruder detected report"
 k="intruder tried to enter the house on time "+str(now.strftime("%Y-%m-%d %H:%M:%S"))
# setup the parameters of the message
 password = "yourpassword"
 msg['From'] = "electricalcoder@gmail.com"
 msg['To'] = "stijovalayil@gmail.com"
 msg['Subject'] = "$$$$ CAUTION $$$ INTRUDER FOUND"
 text = MIMEText(k)
 msg.attach(text) 
# add in the message body
 img_data = open("intruder.jpg", 'rb').read()
 image = MIMEImage(img_data, name=os.path.basename("intruder.jpg"))
 msg.attach(image)
 
 
# 
 
#create server
 server = smtplib.SMTP('smtp.gmail.com: 587')
 
 server.starttls()
 
# Login Credentials for sending the mail
 server.login(msg['From'], password)
 
 
# send the message via the server.
 server.sendmail(msg['From'], msg['To'], msg.as_string())
 
 server.quit()
 
 print("successfully sent email to personal account")
