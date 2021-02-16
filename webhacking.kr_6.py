import base64

user = 'admin'
pw = 'nimda'

b_user = user.encode("utf-8")
b_pw = pw.encode("utf-8")

for i in range(0, 20):
    b_user = base64.b64encode(b_user)
    b_pw = base64.b64encode(b_pw)

print(b_user)
print(b_pw)