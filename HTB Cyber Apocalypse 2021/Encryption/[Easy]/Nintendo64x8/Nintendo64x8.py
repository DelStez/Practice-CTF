import base64

f = open("Nintendo.txt", "r")
content = "".join(f.read().split());
for i in range(8):
    content = base64.b64decode(content)
print(content)
