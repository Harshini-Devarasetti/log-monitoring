import re
import pandas as pd

def prepare_dataset(log_lines):

    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) - (.*)'

    logs = []

    for line in log_lines:
        match = re.match(pattern, line)
        if match:
            timestamp = match.group(1)
            log_level = match.group(2)
            log_message = match.group(3)
            logs.append({'Timestamp': timestamp, 'Level': log_level, 'Message': log_message})

    df = pd.DataFrame(logs)

    return df
    
log_lines = [
    '2023-06-20 10:30:15 INFO - Application started',
    '2023-06-20 10:30:20 ERROR - Database connection failed',
    '2023-06-20 10:30:25 WARNING - Disk space low'
]
dataset = prepare_dataset(log_lines)

print(dataset)
