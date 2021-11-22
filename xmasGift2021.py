import smtplib, random

class SecretSanta:
    def __init__(self):
        self.gmail_user = 'youremail@gmail.com'
        self.gmail_password = 'yourpassword'
        self.friends = [("Alice","alice@gmail.com"),
                        ("Bob", "bob@gmail.com"),
                        ("Cat", "cat@gmail.com")]
        self.server = self.getServer()

    def getServer(self):
        # References:
        # https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
        # https://www.tutorialexample.com/fix-smtplib-smtpnotsupportederror-smtp-auth-extension-not-supported-by-server-python-smtp-tutorial/
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()    
        server.login(self.gmail_user, self.gmail_password)
        return server
        
    def sendEmails(self):
        random.shuffle(self.friends)
        for i in range(len(self.friends)):
            sender, senderEmail = self.friends[i][0], self.friends[i][1]
            receiver = self.friends[(i+1)%len(self.friends)][0]
            message = self.composeMessage(sender, senderEmail, receiver)
            self.server.sendmail(self.gmail_user, senderEmail, message)
            print("Email sent")

    def composeMessage(self, sender, senderEmail, receiver):
        message = "Subject: Christmas Party 2021 - Secret Angel\r\n"
        message += "From : Santa Claus <" + self.gmail_user + ">\r\n"
        message += "To : " + sender + "<" + senderEmail + ">\r\n"
        message += "Dear " + sender + ", \n\n"
        message += "You are invited to join Unier's Christmas Party 2021! Details below:\n\n"
        message += "Date: December 26, 2021\n"
        message += "Time: 2pm - late night \n"
        message += "Venue: Doi home\n\n"
        message += "You will be " + receiver + "'s secret angel.\n\n"
        message += "Merry Christmas,\nSanta Claus"
        return message
    
secretSanta = SecretSanta()
secretSanta.sendEmails()
