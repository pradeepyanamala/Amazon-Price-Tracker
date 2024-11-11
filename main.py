import os
import smtplib
from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup

load_dotenv()
URL = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL)
html_response = response.text
soup = BeautifulSoup(html_response, "html.parser")
price_tags = soup.find("span", class_="a-price-whole").contents[0]
price = int(price_tags)
if price <= 100:
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_mail = os.getenv("SENDER_MAIL")
    sender_pass = os.getenv("SENDER_PASS")
    receiver_mail = os.getenv("RECEIVER_MAIL")

    subject = "Amazon Price Tracker Alert!"
    body = f"This is a auto generated mail from Amazon Price Tracker. This product {URL} is now at best price."
    email_message = f"Subject: {subject} \n\n {body}"
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_mail, sender_pass)
            server.sendmail(sender_mail,receiver_mail,email_message)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error:{e}")
else:
    print("Price tag not found on the page.")




