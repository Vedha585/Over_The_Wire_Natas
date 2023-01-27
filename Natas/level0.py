import requests
url="http://natas0.natas.labs.overthewire.org"
auth_name = 'natas0'
auth_pass = 'natas0'

r=requests.get(url,auth=(auth_name,auth_pass))
for i in r.iter_lines():
    x=i.decode("utf-8")
    if("password" in x):
        print(i.decode("utf-8"))