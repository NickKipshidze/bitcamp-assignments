extensions = {
    "gif" : "image",
    "jpg" : "image",
    "jpeg" : "image",
    "png" : "image",
    "pdf" : "application",
    "txt" : "text",
    "zip" : "file"
}

file = input("").replace(" ", "").split(".")

if len(file) == 1:
    print(f"application/{file[0]}")
else:
    print(f"{extensions[file[1]]}/{file[1]}")