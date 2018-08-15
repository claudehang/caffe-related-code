import os
import cv2

ori_annot_dir = 'ori-yolo-annot/'
new_annot_dir = 'new-yolo-annot/'
img_dir = 'val-img/'
gt_img_dir = 'gt-img/'

for root, dirs, files in os.walk(ori_annot_dir):
    for file in files:
        nameOfImage = file.replace(".txt", "")
        nameOfImage += '.jpg'
        im = cv2.imread(img_dir + nameOfImage)
        sp = im.shape
        h = sp[0]
        w = sp[1]
        fh1 = open(ori_annot_dir + file, "r")
        fh2 = open(new_annot_dir + file, "w")
        for line in fh1:
            line = line.replace("\n", "")
            # prevent blank lines
            if line.replace(' ', '') == '':
                continue
            splitLine = line.split(" ")
            idClass = splitLine[0]
            # the following are relative values
            rel_x = float(splitLine[1])
            rel_y = float(splitLine[2])
            rel_w = float(splitLine[3])
            rel_h = float(splitLine[4])

            # the following are absolute values
            abs_x = w * rel_x
            abs_y = h * rel_y
            abs_w = w * rel_w
            abs_h = h * rel_h

            # calculate the new format of annotation to restore
            left  = int(max(abs_x - 0.5 * abs_w, 0))
            top   = int(max(abs_y - 0.5 * abs_h, 0))
            right = int(min(abs_x + 0.5 * abs_w, w))
            bot   = int(min(abs_y + 0.5 * abs_h, h))

            cv2.rectangle(im, (left, top), (right, bot), (0, 0, 255), 3)
            cv2.imwrite(gt_img_dir + nameOfImage, im)

            write_down = idClass + " %d %d %d %d\n" % (left, top, right, bot)
            fh2.write(write_down)
        fh2.close()
