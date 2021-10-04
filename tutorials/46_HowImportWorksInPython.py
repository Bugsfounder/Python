# import sklearn as sk
# import sys
from sklearn.ensemble import RandomForestClassifier

# from file2 import a # not good practice always imports file like import filename
import file2

print(RandomForestClassifier())
print(file2.a)
print(file2.jokeFunction("Jokers"))
# print(a)
# print(sys.path)
# print(sk.__version__)
