import pickle

# PICKLING A PYTHON OBJECT
# cars = ["Audi", "BMW", "Range Rower", "Ferrari"]
# file = "mycar.pkl"
# fileobj = open(file, "wb")
# pickle.dump(cars, fileobj)
# fileobj.close()


# UNPICKLING A PYTHON OBJECT
file = "mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
print(mycar)

# pickle.load() - takes file object and return corresponding python format (readable )
# pickle.loads() - takes the binary format and returns python format
# pickle.dumps() - takes the variable and returns binary string
