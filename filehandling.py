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
#count

'''
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
l = [i.split() for i in fh.readlines() 
            if i.startswith("From") and i.find("@")>0 and len(i.split())>2]
for i in l:
    print i[1]
    count+=1
print "There were", count, "lines in the file with From as the first word"
'''