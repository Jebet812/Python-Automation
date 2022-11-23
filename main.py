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

# Extracting Hacker News Stories

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get (url)
    content = response.content
    soup =  BeautifulSoup(content, 'html.parser')
    for i,tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign' : ''})):
        cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text != 'More' else '')
    return(cnt)
    
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>') #End of body add email lines
content += ('<br><br>>End of Message')  #Add two lines the end of message line
    
    
#sending the email

print('Composing email...')

SERVER = 'smtp.gmail.com' #the smtp server
PORT = 587 #port number (in this case gmail)
FROM = 'xyz@gmail.com' #emai l to send email from
TO = 'xyz@gmail.com' #email to send to
PASSWORD = '****' #the from's email password

message = MIMEMultipart()

message['Subject'] = 'Top News Hacker News [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) +'-' + str(now.year)
message['From'] = FROM
message['To'] = TO

message.attach(MIMEText(content, 'html')) #adding content to email

print('Initializing Server...')

server = smtplib.SMTP(SERVER, PORT)  #initializing a server
server.set_debuglevel(1) #see error messages
server.ehlo()
server.starttls()
server.login (FROM, PASSWORD) #log in to from
server.sendmail(FROM, TO, message.as_string()) #send email

print('Email Sent Successfully...')
server.quit()









