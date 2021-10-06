# Oh Soldier Prettify My Folder

# path, dictionary , file, format
# path mai jitne bhi files hai unsabhi ka pehla letter capital karna hai agar us file
# ka naam harry.txt mai maujood nahi hua to aur jitne bhi jpg files hai un sabhi ka
# naam kuchh bhi ho jaise :- sd.jpg, cd.jpg etc in sabhi to as a counting numbers 1.jpg, 2.jpg karna hai

# def solder("c://", "harry.txt", "jpg"):
import os


def solder(path, filename, extension):
    pass


path = "TestFile/"
filename = "TestFile/nodel.txt"
extension = ".jpg"

# print(os.listdir(path))
allFiles = os.listdir(path)
f = open("TestFile/nodel.txt")
allContent = f.read()
f.close()
notToChange = allContent.split("\n")
os.chdir("TestFile")
for i in allFiles:
    fName = i.split(".")[0]
    ext = i.split(".")[1]
    print(fName, ext)
    # for nFile in notToChange:
    j = 0
    # while j in range(len(notToChange)):
    try:
        if fName != ext:
            os.rename((fName + "." + ext), (fName).capitalize())

        if ext == "jpg" or fName != ext:
            j += 1
            os.rename((fName + "." + ext), (str(j)))
    except Exception as error:
        print(error)
