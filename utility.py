import re
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

log_lines = [
    "test 2023-06-20 10:30:15 INFO - Application started",
    'abc 2023-06-20 10:30:20 ERROR - Database',
    'xyz 2023-06-20 10:30:25 WARNING - Disk space low'
]

pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+)'

logs = []

for line in log_lines:
    
        logs.append({'content': line})

df = pd.DataFrame(logs)
print(df)

df[['Timestamp', 'level']] = df['content'].str.extract(pattern)

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