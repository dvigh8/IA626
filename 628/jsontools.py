import os,json

class filereader:
    def __init__(self,datadir):
        self.datadir = datadir
        self.dirok = os.path.isdir(self.datadir)
        if self.dirok:
            self.fl = sorted(os.listdir(self.datadir),key=lambda x : int(x.split('.')[-1]))
        else:
             self.fl = []
             self.log("not a vaild directory - " + self.datadir)
        self.glc = 0
        self.flc = 0
    def readJSON(self):
        
        if self.dirok:
            for filename in self.fl:
                ln = 0
                fp = self.datadir + filename
                canopen = False
                try:
                    f = open(fp,'r')
                    canopen = True
                except:
                    self.log("could not open file path " + fp)
                if canopen:
                    fs = f.read()
                    #print fs
                    fs = fs.split("\n")
                    self.glc = 0
                    self.flc = 0
                    for line in fs:
                        lineok = False
                        try:
                            dl = json.loads(line)
                            self.glc += 1
                            lineok = True
                        except Exception as e:
                            self.flc+=1
                            self.log(str(e) + line)
                        if lineok:
                            yield dl
                       
                        ln +=1
    def log(self,msg):
        print msg

class sensorMinMaxSet:
    def setupObject(self):
        self.name = ''
        self.min = []
        self.max = []
        self.tfs = []
    def initData(self):
        for fn in self.tfs:
            self.min.append(None)
            self.max.append(None)
    def addRow(self,row):
        n =0
        for fn in self.tfs:
            if fn in row.keys():
                self.addValue(row[fn],n)
                n+=1
            
    def addValue(self, value,n):
        valueok = False
        try:
            value =  float(value)
            valueok = True
        except:
            pass
        #print value
        if valueok:
            if self.min[n] is None or value < self.min[n]:
                self.min[n] = value
            if self.max[n] is None or value > self.max[n]:
                self.max[n] = value
        
    def show(self):
        n=0
        print self.name
        for fn in self.tfs:
            
            print fn
            print "    Min: " + str(self.min[n])
            print "    Max: " + str(self.max[n])
            n+=1
class tempMinMax(sensorMinMaxSet):
    def __init__(self):
        self.setupObject()
        self.name = 'temps'
        self.tfs = ['temp_1','temp_2','temp_3','temp_4','temp_5','temp_6','temp_7','temp_8','temp_9']
        self.initData()

