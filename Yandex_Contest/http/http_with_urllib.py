from urllib import request

response = request.urlopen('http://127.0.0.1:7777/')

print(response.status)
