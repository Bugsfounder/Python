# PYTHON PRACTICE PROBLEM 7 (MEDIUM, 20 POINTS)
# Search Engine

# Problem Statement:-
# You are given few sentences as a list (Python list of sentences). Take a query
# string as an input from the user. You have to pull out the sentences matching this
# query inputted by the user in decreasing order of relevance after converting every
# word in the query and the sentence to lowercase. The most relevant sentence is the
# one with the maximum number of matching words with the query.

# Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

# Input:
# Please input your query string

# “Python is”

# Output:
# 3 results found:

# 1. python is not python snake
# 2. python is good
# 3. Python is cool

"""
Author: Manisha
Date: 09/10/2021
Purpose: Python Practice
"""


# Create a search function for search a query from a list of sentences
# def search(sentences, query):
#     """
#     This function is for search in a list of sentences for a query
#     :param sentences:
#     :param query:
#     :return: result list
#     """
#     result = []
#     for i in range(len(sentences)):
#         sentence = sentences[i].split(" ")
#         for j in range(len(sentence)):
#             if sentence[j].lower() == query.lower():
#                 result.append(sentences[i])
#                 break
#     return result
#
#
# # printList function is just take a list as parameter and print the list in a good manner with sl number
# def printList(lst):
#     """
#     This function is used for printing a list with sl number
#     :param lst:
#     :return: nothing but it printing the list elements
#     """
#     if len(lst) > 0:
#         for i in range(len(lst)):
#             print(f"{i + 1}. {lst[i]}")
#     else:
#         print("No Result Found")


def matchingWords(sentence1, sentence2):
    words1 = set(sentence1.split(" "))
    words2 = set(sentence2.split(" "))
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


# Main function here
if __name__ == '__main__':
    try:
        sentences = ["Python is cool", "python is good", "python is not Python snake", "Harry Bhai Bahut Achhe hai",
                     "CodeWithHarry is the best Channal for Coders", "Flask is a Python Framework",
                     "Django is a Python Framework", "Programming is the best", "Talk is Cheap Show me the code"]
        query = input("Enter Query For Search: ")
        scores = [matchingWords(query, sentence) for sentence in sentences]

        sortedSentencesScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)]

        print(f"{len(sortedSentencesScore)} results found")
        for score, item in sortedSentencesScore:
            # print(f" \"{item} \" with a score of {score}")
            print(item)

    except Exception as error:
        print("Something went wrong")
