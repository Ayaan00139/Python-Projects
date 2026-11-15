import re
fullurl = input("Whats Your Twitter Url? ").strip()

#---------------------------BEFORE---------------------

#https://x.com/Ayaan12001323

# username=re.sub(r"^(https?://)?(www\.)?x\.com/","",url)
# print(username)

# username=url.removeprefix("https://x.com/") # but this if a user gives whole paragraph it 
# print(username)                          #will come with the usrrname so we use remove prefix

#---------------------------After---------------------

temp,url=fullurl.split("https")
if matches:=re.search(r'^(?:https)?://(?:www\.)?x\.com/([a-zA-Z0-9_]+)',url,re.IGNORECASE):
    print(f"Username:",matches.group(1))

