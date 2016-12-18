import sys
import hashlib
def main():
    inp = "ojvtpuvg"
    count = 0
    i = 0
    while count < 8 :
        hsh = hashlib.md5((inp+str(i)).encode('utf-8')).hexdigest()
        if hsh[0:5]=="00000":
            print(hsh[5])
            count += 1
        i += 1
        #print(hsh[0:5])
if __name__ == "__main__":
    main()
