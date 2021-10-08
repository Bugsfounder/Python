# Oh Soldier Prettify My Folder

# path, dictionary , file, format
# path mai jitne bhi files hai unsabhi ka pehla letter capital karna hai agar us file
# ka naam harry.txt mai maujood nahi hua to aur jitne bhi jpg files hai un sabhi ka
# naam kuchh bhi ho jaise :- sd.jpg, cd.jpg etc in sabhi to as a counting numbers 1.jpg, 2.jpg karna hai

# def solder("c://", "harry.txt", "jpg"):

import os


def soldier(path, file, formate):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == formate:
            os.rename(file, f"{i}{formate}")
            i += 1


soldier(r"F:\tezt", r"F:\Programming and Cyber Security\Programming\Python\Python\tutorials\nodel.txt", ".txt")
