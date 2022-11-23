# First install external packages
#   - bs4
#   -requests

import requests #http requests

from bs4 import BeautifulSoup #web scrapping

#send email 
import smtplib 
#email body
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

# system date and time manipulation
import datetime

now = datetime.datetime.now() #show appropriate date when email was sent

# email content placeholder

content = ''

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    

 
  