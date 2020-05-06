import requests
from bs4 import BeautifulSoup
import smtplib


#URL of the project to be checked:
URL = "https://www.amazon.es/Apple-MacBook-Air-Ordenador-port%C3%A1til/dp/B0721BNGW7/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=apple+computer&qid=1567633613&s=gateway&sr=8-3"
#Price treshold:
price_treshold = 850

headers = {
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])


    if (converted_price < price_treshold):
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



check_price()
