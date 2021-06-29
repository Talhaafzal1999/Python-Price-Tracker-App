#Python app that Notifies you via Email when the price of a product on Amazon goes below a certain price

import requests    # Requests Library allows you to send HTTP/1.1 requests extremely easily

from bs4 import BeautifulSoup # Beautiful Soup is a Python library for pulling data out of HTML and XML files

import smtplib # Smtp protocol handles sending e-mail and routing e-mail between mail servers


# link to the product on Amazon
URL = 'https://www.amazon.ae/Sony-Alpha-Mirrorless-Camera-ILCE-6600/dp/B081LNXGZ1/ref=sr_1_1_sspa?dchild=1&keywords=sony+a7&qid=1624832848&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTjFKRkFRUVJPVEFMJmVuY3J5cHRlZElkPUEwNDQxMDE0MUo0TVZTR1VaS1ZENiZlbmNyeXB0ZWRBZElkPUEwMTMwNDA2MVU3QlREMVBLMEQ2SSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='


# Define User agent 
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}



def check_price():

    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id ="productTitle").get_text()

    price = soup.find(id ="priceblock_ourprice").get_text()

    converted_price = float(price[4:].replace(",",""))



    if(converted_price < 4399.0):  # If the Price is lower than 4399, the send_mail() function will be called #
        send_mail()

    print(converted_price)

    print(title.strip())

    if (converted_price < 4399.0):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

# Email which will send the message

    server.login('automailer951@gmail.com','notautomailer951')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.ae/Sony-Alpha-Mirrorless-Camera-ILCE-6600/dp/B081LNXGZ1/ref=sr_1_1_sspa?dchild=1&keywords=sony+a7&qid=1624832848&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTjFKRkFRUVJPVEFMJmVuY3J5cHRlZElkPUEwNDQxMDE0MUo0TVZTR1VaS1ZENiZlbmNyeXB0ZWRBZElkPUEwMTMwNDA2MVU3QlREMVBLMEQ2SSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='


    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'automailer951@gmail.com',
        'mariejowe87@gmail.com',  # Email to send the message to 
        msg
    )

    print('HEY EMAIL HAS BEEN SENT!!!')

    server.quit()

# Calling the function
check_price()
