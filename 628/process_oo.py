from jsontools import filereader
from jsontools import tempMinMax
from jsontools import sensorMinMaxSet


tmm = tempMinMax()

fr = filereader('data/')
for row in fr.readJSON():
    tmm.addRow(row)
tmm.show()


