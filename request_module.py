import requests

url = "https://api.github.com/users/Nomantariq12"
req = requests.get(url)
print(req)
print(req.status_code)
data = req.json()
print("Following: ", data["following"])
print("Followers: ", data["followers"])
print("Public Repositories: ", data["public_repos"])
print("The Owner of this repository is ", data["name"], "and The total number of public repositories are ", data["public_repos"])