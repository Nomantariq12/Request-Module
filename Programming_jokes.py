import requests

#The url from where we get jokes
url = "https://official-joke-api.appspot.com/jokes/programming/random"
#Get API end point response
req = requests.get(url)
data = req.json()[0]
print(data)
for key in data:
	print(key, " : ", data[key])