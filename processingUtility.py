import re
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

df = search.process_log()

# Print the updated DataFrame
print(df)

#number of lines
print(df.shape[0])

msg = MIMEMultipart()
msg['From'] = 'from.com'
msg['To'] = 'to.com'
msg['Subject'] = 'Log Summary'

if df.shape[0]<=15:
	html = df.to_html()
	body = MIMEText(html, 'html')
	msg.attach(body)
	
else:
	attachment = MIMEText(df.to_csv(index=False), 'csv')
	attachment.add_header('Content-Disposition', 'attachment', filename='data.csv')
	msg.attach(attachment)

print(msg)