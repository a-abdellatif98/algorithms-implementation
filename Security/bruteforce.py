from Des import DesKey

key0 = DesKey(b"00119584") 
Enc = key0.encrypt(b"Rowina tamer K. ")
print(Enc)
arr = bytes(Enc)
Dec =  key0.decrypt(arr)

def brutrForce():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for o in range(10):
                                for p in range(10):
                                    key = str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)
                                    tempkey = bytes(key)
                                    bruteForceKey = DesKey(tempkey)
                                    bruteForceRes = bruteForceKey.decrypt(arr)
                                    #print(bruteForceRes)
                                    if(bruteForceRes == Dec):
                                        print(key+"    YAY!         "+ bruteForceRes)
                                        return
                                    else:
                                        print(key)

brutrForce()