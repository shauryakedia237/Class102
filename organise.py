import os 
import shutil

from_dir = "users/shauryakedia/Downloads/Images old"
to_dir = "users/shauryakedia/Desktop/images/"

list_of_files = os.listdir(from_dir)

#print(list_of_files)

for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext == " ":
        continue
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "images"
        path3 = to_dir + '/' + "images" + '/' + file_name
        print("path1",path1)
        
        if os.path.exists(path2):
            print("moving" + file_name + ".....")
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("moving" + file_name + ".....")
            shutil.move(path1,path3)
    
