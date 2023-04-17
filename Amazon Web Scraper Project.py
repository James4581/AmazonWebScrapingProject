#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries

from bs4 import BeautifulSoup


# In[2]:


import requests
import smtplib
import time
import datetime


# In[13]:


# Connect to Website

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_6?crid=2YBBHZ48RDNJL&keywords=data%2Banalyst%2Btshirt&qid=1681687220&sprefix=data%2Banalyst%2Btshirt%2Caps%2C95&sr=8-6'


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


page = requests.get(URL, headers=headers)


soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find('span', {'class':'a-offscreen'}).get_text()


print(title)
print(price)




# In[14]:


price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[19]:


import datetime

today = datetime.date.today()

print(today)


# In[20]:


import csv

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
# comment out if run again


# In[22]:


import pandas as pd

df = pd.read_csv(r'C:\Users\James\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


# appending data to the csv


with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[23]:



def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_6?crid=2YBBHZ48RDNJL&keywords=data%2Banalyst%2Btshirt&qid=1681687220&sprefix=data%2Banalyst%2Btshirt%2Caps%2C95&sr=8-6'


    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


    page = requests.get(URL, headers=headers)


    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find('span', {'class':'a-offscreen'}).get_text()
    
    price = price.strip()[1:]
    title = title.strip()
    
    import datetime

    today = datetime.date.today()
    
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if (price < 14):
        send_mail()
        


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[25]:


import pandas as pd

df = pd.read_csv(r'C:\Users\James\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('james.stevens@csuglobal.edu', 'xxxxxxxxxxx')
    
    subject = "The price of the shirt has dropped."
    body = "Go pick up the shirt off Amazon!"
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'james.stevens@csuglobal.edu',
        msg
        
    )

