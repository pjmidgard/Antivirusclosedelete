import subprocess, os, time, binascii, glob, os
for namez1 in glob.glob("*exe"):
	print(namez1)
	closem=0
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
			sdas=sda[0:256]
			sdasb=int(sdas,2)
	with open("save.bin", "rb") as binary_file:
		data1 = binary_file.read()
		s=str(data1)
		lenf1=len(data1)
		sda=bin(int(binascii.hexlify(data1),16))[2:]
		lenf=len(sda)      
		lenf1=len(data1) 
		xc=(lenf1*8)-lenf
		z=0
		if xc!=0:
			while z<xc:
				sda="0"+sda
				z=z+1
		lenf2=len(sda) 
		ww1=0
		ww2=0
		while ww2<lenf2:
			ww1=ww2
			ww2=ww2+256
			sdas1=sda[ww1:ww2]
			sdasb1=int(sdas1,2)
			if sdasb1==sdasb:
				closem=closem+1
	if closem>0:
		print("Malware deleted")
		CREATE_NO_WINDOW = 0x08000000
		subprocess.call(nemez, creationflags=CREATE_NO_WINDOW)
		os.remove(namez1)
		closem=0
	else:
		print("Malware has not founded")
	def destroy(plat):
		if plat == 'win':
			import _winreg
			from _winreg import HKEY_CURRENT_USER as HKCU
			run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
			try:
				reg_key = _winreg.OpenKey(HKCU, run_key, 0, _winreg.KEY_ALL_ACCESS)
				_winreg.DeleteValue(reg_key, 'br')
				_winreg.CloseKey(reg_key)
			except WindowsError:
				pass
		elif plat == 'nix':
			pass
		elif plat == 'mac':
			pass
		os.remove(sys.argv[0])
		sys.exit(0) 
os.system("pause")

