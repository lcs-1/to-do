contents = ["jaadfdf dsfndsjfdsnf","adsajfjdsh","sadsjo"]
filenames = ["doc.txt","report.txt","files.txt"]

for content,filename in zip(contents,filenames):
    file = open(f"../files/{filename}",'w')
    file.write(content)