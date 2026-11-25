import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    try:
        _,temp=s.split("src=")
        url=re.search(r'^"(https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9]+)"',temp)
        url=url.group(1).strip()
        assert "</iframe>" in s
        url=url.replace("/embed","")
        if "http://" in url:
            url=url.replace("http","https")
        if "www." in url:
            url=url.replace("www.","")
        url=url.replace("youtube.com","youtu.be")
        return url
    except:
        return None
if __name__ == "__main__":
    main()
