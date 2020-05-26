from Crypto.Cipher import DES
   
def go():
    cipher = DES.new("00945678")
    plain_text = "ahmedmoh"

    encrypted_data = cipher.encrypt(plain_text)
    print (encrypted_data)

    decrypted_data = cipher.decrypt(encrypted_data)
    print(decrypted_data)
    
    print("lets start")

    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    key = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)
                                    cipher = DES.new(key)
                                    bruteForceRes = cipher.decrypt(encrypted_data)
                                    #print(bruteForceRes)
                                    if(bruteForceRes==plain_text):
                                        print(key+"    Congrats         "+ bruteForceRes)
                                        return
                                    else:
                                        print("notyet   " + key)

def main():
    go()

if __name__ == "__main__":
    main()
   