filenames = ["1.doc","1.presentation","1.text"]

newfilenames = [item.replace('.','-') + '.txt' for item in filenames]

print(newfilenames)