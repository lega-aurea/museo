
"""
import os

root = os.getcwd()

Files = []
for subdir, dirs, files in os.walk(root):
    for file in files:
        filepath = subdir + os.sep + file

        if file == "ribes.png":
            continue

        elif file.endswith(".png"):
            Files.append([filepath, subdir+os.sep])

i = 0
for file in Files:
    os.rename(file[0], file[1]+str(i)+".png")
    i+=1
"""


start = "<ul>"
ite = 59
for i in range(ite+1):
    start += "<li><img src=\""+str(i)+".png\"></li>"

with open("product.txt", "w") as a:
        
    a.write(start)
