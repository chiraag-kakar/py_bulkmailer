import pandas as pd
import smtplib
import os
import imghdr
from email.message import EmailMessage

# EMAIL_ADDRESS = os.environ.get('chiraagkakar@gmail.com')
# EMAIL_PASSWORD = os.environ.get('****************')


# e = pd.read_excel("Email.xlsx")
# emails = e['Emails'].values

msg = EmailMessage()
msg['Subject'] = 'Hey Sweety!'
msg['From'] = 'chiraagkakar@gmail.com'

# for email in emails:
msg['To'] = 'ck2222@cse.jgec.ac.in'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('chiraagkakar@gmail.com', EMAIL_PASSWORD)
server.send_message(msg)
server.quit()

