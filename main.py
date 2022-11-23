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
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get (url)
    content = response.content
    soup =  BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'yalign' : ' '})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        return(cnt)
    
    cnt = extract_news('https://news.ycombinator.com/')
    content += cnt
    content += ('<br>------<br>') #End of body add email lines
    content += ('<br><br>>End of Message')  #Add two lines the end of message line
    
    
#sending an email
