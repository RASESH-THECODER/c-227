
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption")
    msg=input("enter your message")
    key=int(input("enter key(1-94): "))
    encrypted_text=""
    for i in range(len(msg)):
        temp=(ord(msg[i])+key)
        if (temp>126):
            temp=temp-127+32


        encrypted_text+=chr(temp)
    print("encrypted: "+encrypted_text)

    main()


    


def decryption():
    print("decryption")
    print("message can only be lower or uppercase alphabets")
    encrp_msg=input("enter encrypted_text")
    decrp_key=int(input("enter key(1-9"))
    descrypted_text=""
    for i in range(len(encrp_msg)):
        temp=(ord(encrp_msg[i])-decrp_key)
        if (temp<32):
            temp=temp-127-32


        descrypted_text+=chr(temp)
    print("descrypted: "+descrypted_text)



    
    

        
if __name__ == "__main__":
    main()
