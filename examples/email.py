import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = 'worldheraldbot@gmail.com'
you = ['cody.winchester@owh.com', 'matt.wynn@owh.com']
pw = #pw goes here

text = "Hello there, mates!"

msg = MIMEMultipart('alternative')
msg['Subject'] = 'Test email'
msg['From'] = "World-Herald Bot"
html = "<html><head><style>* { font-family:Verdana,sans-serif; }</style></head><body>" + text + "</body></html>"
wut = MIMEText(html, 'html')
msg.attach(wut)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(me, pw)
server.sendmail(me, you, msg.as_string())
server.quit()