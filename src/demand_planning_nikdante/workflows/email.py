import smtplib, ssl
from smtplib import SMTP_SSL
class Email:

    def __init__(self) :
        self.smtp_server = "smtp.gmail.com"
        self.port = 587  # For starttls
        self.password="aewonugjjdtsnkmr" 
        self.sender_email = "securesally@gmail.com"
        self.context = ssl.create_default_context()  
    
    def send_mail(self,receiver_email,message):
        server = SMTP_SSL(host=self.smtp_server, port=587)
        server.ehlo() # Can be omitted
        server.starttls(context=self.context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(self.sender_email,self.password)
        server.sendmail(
        receiver_email, 
        self.sender_email, 
        message)
        server.quit()

      