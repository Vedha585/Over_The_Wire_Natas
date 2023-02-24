import requests
import base64
url="http://natas8.natas.labs.overthewire.org"
auth_user="natas8"
auth_pass="a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB"

encoded_secret="3d3d516343746d4d6d6c315669563362"


def secret_decode():
    sec=base64.b64decode(bytes.fromhex(encoded_secret).decode('utf-8')[::-1]).decode('utf-8')
    print(sec)


decoded_sec=secret_decode()
params={'secret':decoded_sec,'submit':'submit'}
r=requests.post(url,auth=(auth_user,auth_pass),data=params)
print(r.text)

#level 9 pass - Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd