import pymysql
import re

f = open('small_log.txt','r')

data = f.read()
d = {}
lines = data.split("\n")
i=0
arr = []
for line in lines:
    cols = re.sub(" +", " ", line).split(" ")
    # YYYY-MM-DD HH:MM:SS
    '''
    if cols[0] in d.keys():
        d[cols[0]] += 1
    else:
        d[cols[0]] = 1
    '''
    if cols[0] != '' and cols[1] != '' and cols[2] != '':

        service = cols[4].split("[")[0]
        #print service
        msg = ' '.join(cols[5:])
        second = cols[2].split(':')[2]
        i+=1
        #part 1
        # print (second + ' ' + service + ' ' + msg)

        #part 2 SELECT service_name, msg FROM small_log WHERE second > 30 AND service_name = 'CRON'
        # if int(second) > 30 and service == "CRON":
        #     print(service + ' ' + msg)

        #part 3 SELECT service_name, msg FROM small_log WHERE msg LIKE '%121.18.238.31%' ORDER BY second
        if '121.18.238.31' in msg:
            arr.append(second + ' ' + service + ' ' + msg)
for x in sorted(arr):
    print (x[3:])
#end part 3
