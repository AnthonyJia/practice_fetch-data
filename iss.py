import requests
import json
import datetime

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

data = response.json()

timestamp = data['timestamp']
# Convert timestap to human readable date and time (out of epoch)
date = datetime.datetime.fromtimestamp(timestamp)
dtime = date.strftime('%Y-%m-%d-%H:%M:%S')

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

print(dtime)
print(longitude)
print(latitude)

lines = [dtime, "\n", longitude, "\n", latitude]

with open('/data/output.txt', 'w') as f:
    f.writelines(lines)

# container needs a place to write and store output