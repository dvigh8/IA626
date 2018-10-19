import os, json,datetime

datadir = 'data/'

min_temps = {}
max_temps = {}
tfs = ['temp_1','temp_2','temp_3','temp_4','temp_5','temp_6','temp_7','temp_8','temp_9']

start_ts = 9999999999999
end_ts = 0



for filename in sorted(os.listdir(datadir),key=lambda x : int(x.split('.')[-1])):
    #print filename
    fp = datadir+filename
    print "reading " + fp
    canopen = False
    try:
        f = open(fp,'r')
        canopen = True
    except:
        print "    Could not open file " + fp
    if canopen:
        fs = f.read()
        fs = fs.split("\n")
        glc = 0
        flc = 0
        for line in fs:
            try:
                dl = json.loads(line)
                glc+=1
            except:
                flc+=1
            if 'type' in dl.keys():
                if dl['type'] == 'print_reading':
                    if dl['unixtime'] < start_ts:
                        start_ts = dl['unixtime']
                    if dl['unixtime'] > end_ts:
                        end_ts = dl['unixtime']
                    for tf in tfs:
                        if tf in dl.keys():
                            if dl[tf] > -150:
                                if tf not in max_temps.keys():
                                    max_temps[tf] = dl[tf]
                                if dl[tf] > max_temps[tf]:
                                    max_temps[tf] = dl[tf]
                                if tf not in min_temps.keys():
                                    min_temps[tf] = dl[tf]
                                if dl[tf] < min_temps[tf]:
                                    min_temps[tf] = dl[tf]

                if dl['type'] == 'trigger_data':
                    pass
        print "    " + str(glc) + " lines read"
        print "    " + str(flc) + " lines failed"
print max_temps
print min_temps
print datetime.datetime.fromtimestamp(int(start_ts)).strftime('%B %d, %Y')
print datetime.datetime.fromtimestamp(int(end_ts)).strftime('%B %d, %Y')
