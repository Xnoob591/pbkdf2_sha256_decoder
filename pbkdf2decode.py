import binascii
import os
import base64 as base
import sys
import time

def decoding(file_name):
    print("============Decoding PBKDF2 hash...==================")
    if os.path.isfile(file_name):
        try:
            with open(file_name, 'r') as f:
                print("[+] Opening hash file...")
                hash_input= f.read().strip()
                list = hash_input.split('$')
                hash = hash_input.split('$')[2]
                print("[+] Converting HEX hash into binary...")
                binary_hash = binascii.unhexlify(hash)
                print("[+] Encoding binary hash into Base64...")
                encoded_hash = base.b64encode(binary_hash) #part3
                encoded_hash1 = encoded_hash.decode('utf-8')
                list1 = list[0].split(":")  
                algo = list1[1] #part1
                iterations = list1[2] #part2   
                salt = list[1]  #part4
                new_hash = f"{algo}:{iterations}:{salt}:{encoded_hash1}"
                print("[+] prepared hash: ", new_hash)
                print("[+] Preparing hash for Hashcat...")
                with open('encoded.txt', 'w+') as f1:
                    f1.write(new_hash)
                    time.sleep(2)
                print("Encoded hash written to encoded.txt")
                os.system("hashcat -a 0 -m 10900 encoded.txt /usr/share/wordlists/rockyou.txt")
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
    else:
        print("File does not exist. Please provide a valid file path.")
        sys.exit(1)
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 pbkdf2decode.py <pbkdf2_hash>")
        sys.exit(1)
    file_name = sys.argv[1]
    decoding(file_name)   
