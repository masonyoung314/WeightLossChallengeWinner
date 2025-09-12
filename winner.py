from dotenv import load_dotenv
import os
import pandas as pd
import smtplib
import ssl
from email.mime.text import MIMEText

load_dotenv()
# Emails
myEmail = os.getenv("MASON_EMAIL")
herEmail = os.getenv("SOFI_EMAIL")
print(myEmail)
print(herEmail)

#SMTP Password
password = os.getenv("PASSWORD")

serverName = "smtp.gmail.com"
port = 465


def percentChange(startWeight, endWeight):
    return (abs(startWeight - endWeight) / startWeight)

# def calculateWinner():
#     # data = pd.read_csv("weightlossdata.csv") Uncomment when we download csv file with data
#     sofiFinalWeight = data.iat[30, 1]
#     sofiStartWeight = dta.iat[1, 1]
#     masonFinalWeight = data.iat[30, 2]
#     masonStartWeight = data.iat[1, 2]

#     masonChange = percentChange(masonStartWeight, masonFinalWeight)
#     sofiChange = percentChange(sofiStartWeight, sofiFinalWeight)

#     if (sofiChange > masonChange):
#         winner = "Sofía"
#     elif (masonChange > sofiChange):
#         winner = "Mason"    
#     else:
#         winner = "It was a tie...30 more days of challenge."

#     return winner


# officialWinner = calculateWinner()
officialWinner = "Mason"
recipients = [myEmail, herEmail]
messageBody = f"""
Dear Sofía and Mason,

We have finally reached the end of your 30 day challenge. As you are well aware, there have been ups and downs, days of complete discipline, and days of intense cravings. However, all of that effort has not been wasted as you have both worked hard to compete against each other to accomplish one goal-- lose as much weight as possible in 30 days.

I am sure you are both dying to know who won the challenge...and I would be too in your position, but I wanted to take a second to congratulate you both on your journey through this difficult challenge. Remember, no matter who wins this challenge, you are both champions in your own right.

And now, without any further ado, I present to you the winner of Sofía and Mason's 30 Day Weight Loss Challenge...
And the winner is...
Drum roll please...
al;skdjfa;lksdjfal;skdfja;lsdkfjas;dlkfjasdl;fkjasd;flkjasdf;lkjasdflkjasdf;lkajsdf;lkasjdf;laksdjf;alskdjfa;sldkfjasd;lfkjasd;lfkjasd;lfkjasd;flkjasdf;lkjasdf;lkajsdf;lkajsdf (clicky keyboard)























The winner of Sofía and Mason's 30 Day Weight Loss Challenge is {officialWinner}!!!!!!!!!!!!!!!!!!!!
"""

msg = MIMEText(messageBody, 'plain')
msg["From"] = myEmail
msg["To"] = ", ".join(recipients)
msg["Subject"] = "And the winner is..."


with smtplib.SMTP_SSL(serverName, port) as server:
    server.login(myEmail, password)
    server.send_message(msg)


    
    
    