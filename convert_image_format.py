import os
import cv2

in_dir  = 'non-jpg/'
out_dir = 'all-jpg/'
for root, dirs, files in os.walk(in_dir):
    for file in files:
        new_name = os.path.splitext(file)[0] + '.jpg'
        print("processing ==> " + file)
        im = cv2.imread(in_dir + file)
        cv2.imwrite(out_dir + new_name, im)
        print("Finish" + file + '\n\n\n\n')
