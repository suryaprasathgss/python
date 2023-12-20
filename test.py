import os
from datetime import datetime, timedelta

todate = datetime.now().strftime("%Y-%m-%d")

# Calculate yesterday's date
yesterday = datetime.now() - timedelta(days=1)

print(yesterday)