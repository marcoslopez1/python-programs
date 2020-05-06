import requests
from bs4 import BeautifulSoup
import smtplib

#CONF VARIABLES
#Number of digits of the integer price (23 euros means 2 digits)
int_price = 2
#URL of the project to be checked:
URL = "https://www.amazon.es/12-Rules-Life-Peterson-Jordan/dp/0141988517/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=jordan+peterson+12+rules+for+live&qid=1567852125&s=gateway&sr=8-1"
#Price treshold:
price_treshold = 11

headers = {
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}


page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, "html.parser")
str_soup = str(soup)

#Class to search
position_price = str_soup.find('a-size-medium a-color-price offer-price a-text-normal')

#len + spaces in class
price_start = position_price + 58

i = 0
price = 0


while i < int_price:
   increment = int(str_soup[price_start + i])
   price = (price*10) + increment
   i = i+1

#print(price)

if (price < price_treshold):
        gmail_user = 'todolistapp100'
        gmail_password = '100todolistapp'
        sent_from = gmail_user
        to = ['marcoslopezalvarez@gmail.com']
        subject = 'Price has fallen down'

        body = '\nHi there!\n\nThe price of your selected product has fallen down.\nYou can check it out in the next link:\n'+URL+'\n\nCheers!'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.close()
                print 'Email sent!'
        except:
                print 'Something went wrong...'



else:
        print("price is still too high")
        print(price)


