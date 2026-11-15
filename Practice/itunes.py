import requests
import sys
import json

if (len(sys.argv)!=2):
    sys.exit()

# try:
response=requests.get("https://itunes.apple.com/search?entity=song&term=" + sys.argv[1])
obj=response.json()["results"]
for result in obj:
    print(result["trackName"])

# print(obj)