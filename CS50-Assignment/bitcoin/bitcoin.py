import requests
import sys
import json
if not len(sys.argv)==2:
    sys.exit("")
try:
    x=float(sys.argv[1])
except:
    sys.exit("")

api="c83edad8e77ef18038bcd643188da62a0120ef850b513196a76f2576ef255311"
response=requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey="+api).json()
# print(response)
# d=response["data"]["priceUsd"]
# print(d)
d=float(sys.argv[1])*float(response["data"]["priceUsd"])
print(f"${d:,.4f}")
