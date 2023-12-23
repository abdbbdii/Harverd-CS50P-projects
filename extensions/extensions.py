file=input("File name: ").strip().casefold()
if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpeg") or file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")