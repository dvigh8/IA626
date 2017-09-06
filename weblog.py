f = open('weblog.txt','r')

#print f.read()[0:200]
s = f.read()
lines = s.split("\n")

#print len(lines)
data = []



for line in lines:
	row = {}
	cols = line.split(" ")
	row['ip'] = cols[0]
	row['dt'] = cols[3].replace("[","")
	date = row['dt'].split('/')
	time = date[2].split(':')
	tmp = cols[4]
	row['utcoffs'] = tmp.replace("]","")
	row['utcoffdir'] = row['utcoffs'][0]
	row['utcoffint'] = int(row['utcoffs'][1:5])
	
	row['day'] = int(date[0])
	row['month'] = date[1]
	row['year'] = int(time[0])
	row['hour'] = int(time[1])
	row['min'] = int(time[2])
	row['sec'] = int(time[3])
	print (row)
	data.append(row)