import requests

url = "http://njsoly-raz5-ha:8123/api/"
headers = {
    "Authorization": "Bearer ABCDEFGH",
}
response = requests.request("GET", url, headers=headers)

print(response.text)
