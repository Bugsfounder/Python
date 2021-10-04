# CREATE A DICTIONARY AND TAKE INPUT FROM THE USER AND RETURN THE MEANING OF THE WORD FROM THE DICTIONARY

myDict = {
    "apple": "apple is a very testy fruit",
    "mango": "Mango is a very very testy fruit",
    "banana": "Banana is a very healthy fruit",
    "watermelon": "Watermelon is a very testy fruit it available in summer season mostly",
    "Manisha": "Manisha is a very genius girl"
}
print("These are the word available in our dictionary: ")
print(myDict.keys())
print("Enter a value to get meaning of: ", end="")
uesrInput = input()
print(myDict.get(uesrInput))
