import pymysql # run pip install pymysql if this fails
import csv
import time

start = time.time()

with open('snow.csv') as f:
	wifiTable = [{k: str(v) for k, v in row.items()}
		 for row in csv.DictReader(f, skipinitialspace=True)]

print( "Import : " + str(time.time() - start))

conn = pymysql.connect(host='workzone.homeip.net', port=3306, user='ia626', passwd='ia626clarkson', db='ia626', autocommit=True) #setup our credentials
cur = conn.cursor(pymysql.cursors.DictCursor)

cur.execute("CREATE TABLE IF NOT EXISTS `josephd_snow` (\
  `date` varchar(20) NOT NULL,\
  `depth` int(50) NOT NULL,\
  PRIMARY KEY (`date`)\
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4485 ")
cur.execute("TRUNCATE TABLE `josephd_snow`")

blockSize = [200]
for bs in blockSize:
	start = time.time()
	i=0
	sql=''
	tokens = []
	for row in wifiTable:
		sql += "INSERT INTO josephd_snow (`date`,`depth`) VALUES (%s,%s);"
		tokens.extend([row["date"],row["depth"]])
		if i % bs == 0:
			cur.execute(sql,tokens)
			sql = ''
			tokens = []
		i+=1

	if len(sql) > 0:  #handle any leftover SQL queries
		cur.execute(sql,tokens)

	print ("blockSize: " + str(bs) + " - SQL : " + str(time.time() - start))
cur.close()
conn.close()