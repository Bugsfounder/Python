# # importing requests package
import json
import requests
from win32com.client import Dispatch

# def NewsFromBBC():
#     # BBC news api
#     # following query parameters are used
#     # source, sortBy and apiKey
#     query_params = {
#         "source": "bbc-news",
#         "sortBy": "top",
#         "apiKey": "8b24e1ef076f4eeb82db4e8e6d2940c4"
#     }
#     main_url = " https://newsapi.org/v1/articles"
#
#     # fetching data in json format
#     res = requests.get(main_url, params=query_params)
#     open_bbc_page = res.json()
#
#     # getting all articles in a string article
#     article = open_bbc_page["articles"]
#
#     # empty list which will
#     # contain all trending news
#     results = []
#
#     for ar in article:
#         results.append(ar["title"])
#
#     for i in range(len(results)):
#         # printing all trending news
#         print(i + 1, results[i])
#
#     # to read the news out loud for us
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.Spvoice")
#     speak.Speak(results)
#
#
# # Driver Code
# if __name__ == '__main__':
#     # function call
#     NewsFromBBC()


# EXERCISE SOLUTION HERE BY ME

news = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=8b24e1ef076f4eeb82db4e8e6d2940c4")
newsRes = news.json()
allArticles = newsRes['articles']

result = []

for arr in allArticles:
    result.append(arr['title'])

# for item in result:
#     print(item)

for i in range(len(result)):
    print(f"{i + 1}.", result[i])

if __name__ == '__main__':
    i = 0
    while (i < len(result)):
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(f"{str(i + 1)}news is {result[i]}")
        i = i + 1
