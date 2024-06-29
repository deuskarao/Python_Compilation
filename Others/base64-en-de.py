import base64

string1='{"id":1,"admin":true}'
hash=''

out1 = base64.b64encode(string1.encode("utf-8"))
out2 = base64.b64decode(hash.encode("utf-8"))

print(out1.decode())
print(out2.decode())
