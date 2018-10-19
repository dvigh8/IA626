import requests
import json
import csv
from datetime import datetime

def getDayLight(zipcode):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + '&APPID=a6962678a5cba51e8db12b46bc87a867')

    res = json.loads(r.text)
    if res['cod'] == 200:

        return { 'status': 'ok',
    'rise':str(datetime.fromtimestamp(res["sys"]['sunrise'])).split(' ')[1],
    'set':str(datetime.fromtimestamp(res["sys"]['sunset'])).split(' ')[1],
    'riseunix' : res["sys"]['sunrise'],
    'setunix': res["sys"]['sunset'] }

    else:
        return { 'status': 'error'}

with open('ziplist.csv') as f:
    zips = [{k: str(v) for k, v in row.items()}
		 for row in csv.DictReader(f, skipinitialspace=True)]

with open('rise_set.csv', 'w') as csvfile:
    fieldnames = ['zip', 'start','end']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in zips:
        data = getDayLight(row['zip'])
        if data['status'] != 'error':
            writer.writerow({'zip': row['zip'], 'start':data['rise'] ,'end':data['set']})
