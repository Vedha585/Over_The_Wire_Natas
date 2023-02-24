import requests
url="http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"
auth_name = 'natas3'
auth_pass = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'

s=requests.get(url,auth=(auth_name,auth_pass))
print(s.text)
