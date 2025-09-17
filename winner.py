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
    return (abs(startWeight - endWeight) / startWeight) * 100

def calculateWinner():
    data = pd.read_csv("weightlossdata.csv") 
    print(data.head())
    sofiFinalWeight = data.iloc[27].loc["Sofi's Weight (kg)"] 
    sofiStartWeight = data.iloc[0].loc["Sofi's Weight (kg)"]
    masonFinalWeight = data.iloc[27].loc["Mason's Weight (kg)"]
    masonStartWeight = data.iloc[0].loc["Mason's Weight (kg)"]

    masonChange = percentChange(masonStartWeight, masonFinalWeight)
    sofiChange = percentChange(sofiStartWeight, sofiFinalWeight)
    print(masonChange)
    print(sofiChange)

    if (sofiChange > masonChange):
        winner = "Sofía"
        winnerPercentChange = sofiChange
    elif (masonChange > sofiChange):
        winner = "Mason"    
        winnerPercentChange = masonChange
    else:
        winner = "It was a tie...30 more days of challenge."
        winnerPercentChange = sofiChange

    return (winner, winnerPercentChange)

winnerInfo = calculateWinner()
officialWinner = winnerInfo[0]
winnerChange = winnerInfo[1]
recipients = [myEmail, herEmail]

# formatting if it is a tie/not a tie
statement = " each."
noStatement = "."


messageBody = f"""
Dear Sofía and Mason,

We have finally reached the end of your 30 day challenge. As you are well aware, there have been ups and downs, days of complete discipline, and days of intense cravings. However, all of that effort has not been wasted as you have both worked hard to compete against each other to accomplish one goal-- lose as much weight as possible in 30 days.

I am sure you are both dying to know who won the challenge...and I would be too in your position, but I wanted to take a second to congratulate you both on your journey through this difficult challenge. Remember, no matter who wins this challenge, you are both champions in your own right.

And now, without any further ado, I present to you the winner of Sofía and Mason's 30 Day Weight Loss Challenge...
And the winner is...
Drum roll please...
al;skdjfa;lksdjfal;skdfja;lsdkfjas;dlkfjasdl;fkjasd;flkjasdf;lkjasdflkjasdf;lkajsdf;lkasjdf;laksdjf;alskdjfa;sldkfjasd;lfkjasd;lfkjasd;lfkjasd;flkjasdf;lkjasdf;lkajsdf;lkajsdf (clicky keyboard)























The winner of Sofía and Mason's 30 Day Weight Loss Challenge is {officialWinner}!!!!!!!!!!!!!!!!!!!! with %{winnerChange} loss of body weight{statement if winnerInfo == "It was a tie...30 more days of challenge." else noStatement} 

Congratulations!!!!
"""

testmessageBody = f"""
If we were to end the challenge today, my Pequeñita, the result would be...

{officialWinner}, you are the winner!!! as you lost %{winnerChange} of your bodyweight.
"""
msg = MIMEText(testmessageBody, 'plain')
msg["From"] = myEmail
msg["To"] = ", ".join(recipients)
msg["Subject"] = "And the winner is..."


with smtplib.SMTP_SSL(serverName, port) as server:
    server.login(myEmail, password)
    server.send_message(msg)


    
    
    