# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:12:04 2019

@author: hp
"""

import requests, time, smtplib
from bs4 import BeautifulSoup
from notify_run import Notify
from datetime import datetime

url = 'https://www.amazon.co.uk/Wireless-Patuoxun-Computer-Cordless-Adjustment/dp/B01ESZJSUK/ref=pd_bxgy_147_img_2/261-8829968-6337237?_encoding=UTF8&pd_rd_i=B01ESZJSUK&pd_rd_r=56d64070-b8c4-4e7c-a208-3842f6df21b0&pd_rd_w=f0ntx&pd_rd_wg=DQBBQ&pf_rd_p=7a9d3b22-47b7-4932-be38-57f4219c3325&pf_rd_r=68ZRBBKJFKF9Y4M2HZX5&psc=1&refRID=68ZRBBKJFKF9Y4M2HZX5'
dp = 8
URL = url
pnmsg = "Below Euro. " + str(dp) + " you can get your COMPUTER."
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3809.132 Safari/537.36'}

def check_price():

  page = requests.get(URL, headers=headers,)
  soup= BeautifulSoup(page.content,'html.parser')
  
  #--------------------------------------------------------------------------------------
  title = soup.find(id="productTitle").get_text()
  price = soup.find(id="priceblock_ourprice").get_text()
  main_price = price[1:2]
  main_price = int(main_price)
  price_now = int(main_price)

  #VARIABLES FOR SENDING MAIL AND PUSH NOTIFICATION---------------------------------------
  title1 = str(title.strip())
  main_price1 = main_price
  print("NAME : "+ title1)
  print("CURRENT PRICE : "+ str(main_price1))
  print("DESIRED PRICE : "+ str(dp))

  count = 0
  if(price_now <= dp):
    send_mail()
    push_notification()
  else:
    count = count+1
  print("Rechecking... Last checked at "+str(datetime.now()))

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login('rakulle@gmail.com','tyyeakwphgocrncc')
  subject = "Price of COMPUTER fallen down below Rs. "+str(dp)
  body = "Hey Stefan! \n The price computer euros."+str(dp)+".\n So, hurry up & check the amazon link right now : "+url
  msg = f"Subject: {subject} \n\n {body} "
  server.sendmail('rakulle@gmail.com', 'nicoleta.nastasia@gmail.com', msg)
  
  
  
  
  print("HEY STEFAN, EMAIL HAS BEEN SENT SUCCESSFULLY.")
 
  server.quit()

#Now lets send the push notification-------------------------------------------------
def push_notification():
  notify = Notify()
  notify.send(pnmsg)
  print("HEY STEFAN, PUSH NOTIFICATION HAS BEEN SENT SUCCESSFULLY.")
 
  print("Check again after an hour.")
#Now lets check the price after 1 min ----------------------------------------------- 
count = 0
while(True):
  count += 1
  print("Count : "+str(count))
  check_price()
  time.sleep(1000)