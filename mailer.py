#!/usr/bin/env python3
# Import smtplib for the actual sending function
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

from_addr = ''
sent_from = ''
subject = ''

#get gmail password
try: 
    with open('password.txt', 'r') as file:
        gmail_password = file.read()
except Exception as e: 
    print(e)

#parse msg txt
try:
    with open('msg.txt', 'r') as file:
        body = file.read()
except Exception as e: 
    print(e)


email_text = """\
From: %s
To: %s
Subject: %s

%s,

%s
""" 

#setup connection to gmail
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(from_addr, gmail_password)
    print("Connection to email server setup")
except Exception as e: 
    print(e)

#parse emails and sent msg
try:
    with open('people.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            print(row)
            to_addr = row[1]
            to_name = row[0]
            msg_txt=email_text % (from_addr, to_addr, subject, to_name, body)
            try:
                server.sendmail(sent_from, to_addr, msg_txt)
                print ('Email sent')
            except Exception as e:
                print('error sending msg: %s' % e)
except Exception as e: 
    print("error with CSV file")
    print(e)    

#clean up
server.close()