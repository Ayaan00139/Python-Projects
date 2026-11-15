extension=input("Enter File Name With Extension Seprated By dot: ").strip().lower()

while True:
    if "." in extension:
        name,extension=extension.split(".",1)
    else:
        break
extension=extension.strip()
if extension in ("jpeg","jpg"):
    print(f"image/jpeg")
elif extension in ("gif","png"):
    print(f"image/{extension}")
elif extension=="txt":
    print(f"text/plain")
elif extension in ("zip","pdf"):
    print(f"application/{extension}", end="")
else:
    print(f"application/octet-stream", end="")

