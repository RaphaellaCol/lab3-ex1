import smtplib
fromname = 'Raphy'
fromaddr = 'raphycol.info3180@gmail.com'
toname = 'Me'
toaddr  = 'raphycol.info3180@gmail.com'
subject = 'Info3180- Web Dev'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
msg = 'Hello'
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'raphycol.info3180@gmail.com'
password = 'maehrmyaqvjrxutw'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()