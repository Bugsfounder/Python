import requests

# r = requests.get("https://docs.python-requests.org/en/latest/")
r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# print(r.text)
fetchContent = r.text
# print(fetchContent)
# print(r.status_code)

url = "https://reqres.in/api/users"
data = {
    "email": "bugs@bugsfounder.com",
    "password": "bugs"
}

r2 = requests.post(url=url, data=data)
print(r2.text)
