import subprocess, os, time, random, binascii
closem=0
namez1 = input("Please, enter name of malware/software? ")
nemez='taskkill /F /IM '+namez1
#p = subprocess.Popen('pause.exe')
with open(namez1, "rb") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        s=str(data)
        lenf1=len(data)
        sda=bin(int(binascii.hexlify(data),16))[2:]
        lenf=len(sda)      
        lenf1=len(data) 
        xc=(lenf1*8)-lenf
        z=0
        if xc!=0:
            while z<xc:
                sda="0"+sda
                z=z+1
        NumToGuess = random.randint(0, 255)
        sdas=sda[0:8]
        sdasb=int(sdas,2)
        if sdasb==NumToGuess:
            closem=1
time.sleep(2)
if closem==1:
    print("Malware deleted")
    CREATE_NO_WINDOW = 0x08000000
    subprocess.call(nemez, creationflags=CREATE_NO_WINDOW)
    os.remove(namez1)
if closem==0:
    print("Malware has not founded")
    

