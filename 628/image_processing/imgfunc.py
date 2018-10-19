import os, json,time,requests
import PIL.ExifTags,PIL.Image

def getImgData(fp):
    canopen = False
    try:
        f = open(fp,'r')
        canopen = True
    except:
        pass
    if canopen:
        data = {}
        img = PIL.Image.open(fp)
        data['exif'] = getExif(img)
        data['rgb'] = getRGB(img)
        data['citystate'] = getCityState(img)
        return data
    return {}
def getExif(img):
    exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }
    exif['UserComment'] = ''
    return exif
def getRGB(img):
    r, g, b = 0, 0, 0
    count = 0
    img_data = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            tempr,tempg,tempb = img_data[x,y]
            r += tempr
            g += tempg
            b += tempb
            count += 1
    return {'red':r/count, 'green':g/count, 'blue': b/count, 'total':count}
def getCityState(lat,lon):
    key = 'AIzaSyCp144XRaSrBf-VppKfMkAW3V7ZOUr0XSk'
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(lat)+','+str(lon)+'&key='+key)
    data = json.loads(r.text)
    buf = {}
    if len(data['results']) > 0:
        for part in data['results'][0]['address_components']:
            if "administrative_area_level_3" in part['types']:
                buf['city'] = part['long_name']
            if "administrative_area_level_1" in part['types']:
                buf['state'] =  part['long_name']

    return buf
