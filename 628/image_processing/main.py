###unit tests
import imgfunc
import time
import PIL.ExifTags,PIL.Image
import os
import threading


last = 0
interval = 1
while True:
    if time.time()-last> interval:
        last = time.time()
        for filename in sorted(os.listdir('input')):
            if '.jpg' in filename.lower():
                img = PIL.Image.open('input/' + filename)
                print (imgfunc.getExif(img))
                img.close()
                os.rename('input/' + filename,'tmp/' + filename)



# start = time.time()
# img = PIL.Image.open('input/20170122_132543.jpg')
# print (time.time() - start)
#
# start = time.time()
# print (imgfunc.getExif(img))
# print (time.time() - start)
#
# start = time.time()
# print (imgfunc.getRGB(img))
# print (time.time() - start)
#
# start = time.time()
# print (imgfunc.getCityState(44.545646,-75.67675))
# print (time.time() - start)
