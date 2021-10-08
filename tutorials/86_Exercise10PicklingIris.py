import pickle

dataRead = open("iris.data")

allDataContent = ""
while dataRead.readline():
    allDataContent = dataRead.read()

contentArray = allDataContent.split("\n")

# PICKLING A PYTHON OBJECT
# file = "irislist.pkl"
# fileObj = open(file, "wb")
# pickle.dump(contentArray, fileObj)
# fileObj.close()

# UNPICKLING A PYTHON OBJECT
file = "irislist.pkl"
fileData = open(file, "rb")
resData = pickle.load(fileData)
print(resData)
