import operator
#The following code reads csv data from test.csv into memory as a list of #dictionaries called ‘data’ . Example:
#[{'col2': 2, 'col3': 3, 'col1': 1}, {'col2': 5, 'col3': 6, 'col1': 4}]
import csv
with open('wifi.csv') as f:
	data = [{k: str(v) for k, v in row.items()}
		for row in csv.DictReader(f, skipinitialspace=True)]

count = {}
minutes = {}

for row in data:
	minute = str(row['FirstSeen'].split(' ')[1].split(':')[1]) # how to find minutes
	h = str(row['FirstSeen'].split(' ')[1].split(':')[0]) # how to find hours
	if h in count.keys():
		count[h] += 1
	else:
		count[h] = 1
	if minute in minutes.keys():
		minutes[minute] += 1
	else:
		minutes[minute] = 1

ids = {}
macids = {}
for row in data:
	ssid = row['SSID']
	if 'CPH' not in ssid:
		continue
	else:
		macids[row['MAC'][:8]] = 0
		if ssid in ids.keys():
			ids[ssid] += 1
		else:
			ids[ssid] = 1
print ('there are ' + str(len(macids)) + ' different manufacturers for CPH')

macids = {}
for row in data:
	macids[row['MAC']] = int(row['Channel'])

sortedmac = sorted(macids.items(),key=operator.itemgetter(1))

channels = {}
for m, c in sortedmac:
	if c in channels.keys():
		channels[c] += 1
	else:
		channels[c] = 1
print(channels)


