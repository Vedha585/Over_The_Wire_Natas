import requests
url="http://natas2.natas.labs.overthewire.org/files/users.txt"
auth_name = 'natas2'
auth_pass = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'

s=requests.get(url,auth=(auth_name,auth_pass))
print(s.text)

