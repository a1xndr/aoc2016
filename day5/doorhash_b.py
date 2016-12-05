import sys
import hashlib
def main():
    inp = "ojvtpuvg"
    count = 0
    i = 0
    password = ['\0','\0','\0','\0','\0','\0','\0','\0']
    while count < 8 :
        hsh = hashlib.md5((inp+str(i)).encode('utf-8')).hexdigest()
        if hsh[0:5]=="00000":
            print(hsh)
            if ( ord(hsh[5]) - ord('0') < 8 and ord(hsh[5]) - ord('0')>= 0):
                pos = int(hsh[5])
                if(password[pos] == "\0"):
                    count += 1;
                    password = list(password)
                    password[pos] = hsh[6]
                print(''.join(password))
        i += 1
        
if __name__ == "__main__":
    main()
