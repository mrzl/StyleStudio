import sys
import os
from PIL import Image

def imagesize(image):
    im = Image.open(image)
    return im.size

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Not enough command line parameter provided.")
        print('try \'python cutter.py image.png 10 20\' where 10 is the amount of tiles in x direction, 20 the amount in y direction')
        sys.exit(1)

    param = sys.argv[1]
    width, height = imagesize(param)
    param = param[:-4]

    xres = int(sys.argv[2])
    yres = int(sys.argv[3])

    tilesizex = int(width) / xres
    tilesizey = int(height) / yres

    max = xres * yres
    count = 0

    for i in xrange(xres):
        for j in xrange(yres):
            x = i * tilesizex
            y = j * tilesizey
            name = 'out/' + str(param) + '_' + str(i).zfill(3) + '_' + str(j).zfill(3) + '.png'
            cmd = 'convert ' + param + '.png[' + str(tilesizex) + 'x' + str(tilesizey) + '+' + str(y) + '+' + str(x) + '] ' + name
            os.system(cmd)

            perc = count / float(max) * 100.0
            print(str(perc) + '%')

            count += 1

    print('Finished.')