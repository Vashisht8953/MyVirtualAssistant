import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "munivashisht895330@gmail.com"
toaddr = "vashisht11813502@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()
print("hiii")

# storing the senders email address
msg['munivashisht895330@gmail.com'] = fromaddr

# storing the receivers email address
msg['vashisht11813502@gmail.com'] = toaddr

# storing the subject
msg['Subject'] = "Regarding file attachment"

# string to store the body of the mail
body = "this is email from vashisht"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "flower.jpg"
attachment = open("C:\\Users\\Vashisht\\OneDrive\\Pictures\\Camera Roll\\flower.jpg", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "password")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
