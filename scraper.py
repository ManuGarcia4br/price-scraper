import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com.br/Chainsaw-Man-Vol-Tatsuki-Fujimoto/dp/6559820327/ref=d_pd_sbs_sccl_3_3/135-9611245-5546835?pd_rd_w=PfHsz&content-id=amzn1.sym.bc536bd6-e72b-44eb-9471-0bedf0517c03&pf_rd_p=bc536bd6-e72b-44eb-9471-0bedf0517c03&pf_rd_r=RBS088PP1YVXYMPDZ9W6&pd_rd_wg=Rh9bh&pd_rd_r=f187f3cc-7017-4c4d-b05c-d3c01d94b47f&pd_rd_i=6559820327&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price<28):
        send_mail()

    print(converted_price)

    print(title.strip())
    
    if(converted_price < 28):
        send_mail()
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('email@gmail.com', apppassword)
    
    subject = 'O preço está abaixo'
    body = 'O link a seguir leva ao produto em promoção https://www.amazon.com.br/Chainsaw-Man-Vol-Tatsuki-Fujimoto/dp/6559820327/ref=d_pd_sbs_sccl_3_3/135-9611245-5546835?pd_rd_w=PfHsz&content-id=amzn1.sym.bc536bd6-e72b-44eb-9471-0bedf0517c03&pf_rd_p=bc536bd6-e72b-44eb-9471-0bedf0517c03&pf_rd_r=RBS088PP1YVXYMPDZ9W6&pd_rd_wg=Rh9bh&pd_rd_r=f187f3cc-7017-4c4d-b05c-d3c01d94b47f&pd_rd_i=6559820327&psc=1'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'email@gmail.com',
        'rxgarcia1998@gmail.com',
        msg
    )
    print('O email foi enviado!')
    
    server.quit()
    
while(True):
    check_price()
    time.sleep(3600)
