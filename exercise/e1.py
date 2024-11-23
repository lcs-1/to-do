import glob

myfilepath = glob.glob("important/*.txt")
for filerou in myfilepath:
    with open(filerou,'r') as file:
        print(file.read().upper())