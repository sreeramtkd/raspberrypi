import requests
import time 
import json
r=requests.get('https://api.thingspeak.com/channels/1933792/feeds.json?api_key=17UDHXE1L6Z4K5FP')
n=json.loads(r.text)
for i in range(len(n['feeds'])):
    print(n['feeds'][i]['created_at'],n['feeds'][i]['field1'],n['feeds'][i]['field2'])
