import requests,json
data = {'location':'USNY1172', 'months': [] }

for i in range(1,13):
    r = requests.get('http://www.intellicast.com/Local/History.aspx?month=' + str(i) + '&location=' + data['location']).text.split('<table id="dailyClimate" class="Container">')[1].split('<div style="clear:both;"></div>')[0].split('<tr')

    tmp = {'number':str(i),'name':r[2].split('<td style="padding-left:5px;">')[1].split('</td>')[0][:3],'days':[]}
    for i in range(2,len(r)):
        day = r[i].split('<td style="padding-left:5px;">')[1].split('</td>')
        tmp['days'].append({'number': day[0][4:],'average_low': day[1][10:].split('&')[0],'average_high': day[2][10:].split('&')[0],'record_low': day[3][10:].split('&')[0],'record_high': day[4][10:].split('&')[0],'average_precipitation': day[5][10:].split('&')[0],'average_snow': day[6][10:].split('&')[0]})
    data['months'].append(tmp)

with open('intellicast_scrape.json','w') as outfile:
    json.dump(data,outfile)

# print(json.dumps(data)) # if wanted prints to console

# Data structure is
# data = {
# "location": "USNY1172",
# "months": [{
#     "number": 1,
#     "name": Jan,
#     "days":[{
#         "number": 1,
#         "average_low": 6,
#         "average_high": 27,
#         "record_low": -27,
#         "record_high": 59,
#         "average_precipitation": 0.08",
#         "average_snow": NA
#       }]
#   }]
# }
