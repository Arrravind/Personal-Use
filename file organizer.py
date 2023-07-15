import os
import shutil

def organize(path):
    files = os.listdir(path)
    for file in files:
        filename,extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    return True
       
pa = input("Enter the path here : ")
if pa in os.listdir():    
    if organize(pa):
        print("File Organized Successfully!!! :)")
    else:
        print("Invalid Path")
else:
    print("Invalid Path")

