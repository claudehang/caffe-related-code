import random
import os 

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] in ['.jpg', '.jpeg', '.png'] :  
                L.append(file)
    return L
 
my_filename=file_name('./fire-images')
 
random.shuffle(my_filename)
f=open('./fire-images/image_list.txt','w')
for i in my_filename:
    f.write(i+"\n")
f.close()
