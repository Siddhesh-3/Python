#File Handling - (open ,do something ,close)

path = r'F:\Python'  # r is for  raw string
import os 
#print(os.listdir(path))
#print(os.getcwd())

files = os.listdir(path)

for file in files:
    if '.txt' in file :
        #print(file)
        fh = open(file)
        content = fh.read()
        if 'secret_key' in content:  #search content
            print(file) #or (path+'//'+file)
            fh.close()
            