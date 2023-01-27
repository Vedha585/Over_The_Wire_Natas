import requests
url="http://natas1.natas.labs.overthewire.org/"
auth_name = 'natas1'
auth_pass = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

r=requests.get(url,auth=(auth_name,auth_pass))
for i in r.iter_lines():
    x=i.decode("utf-8")
    if("password" in x):
        print(i.decode("utf-8"))