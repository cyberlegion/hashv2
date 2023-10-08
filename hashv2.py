import hashlib
import os
count=0
list=['']
raw=['']

while(1):
	temp=input("[+] Enter the Word : (for 'exit' type bye or exit ) : ")
	if(temp=="exit" or temp=="bye"):
		os.system('clear')
		break
		os.system('clear')
		print("- - - - - - - PROGRAM ENDED - - - - - - ")
	if(temp=='clear'):
		os.system('clear')
		continue
	choice=input("\n[+] Hashing Operations :\n1.SHA256\n2.MD5\nExtra Options :--\n3.Save and Display\n4.Don't Save and display\n5.EXIT\n[+] Choose Option : ")
	if choice=='1':
		raw.append(temp)
		temp=hashlib.sha256(temp.encode()).hexdigest()
		list.append(temp)
		count=count+1
		print('\n')
	elif choice=='2':
		raw.append(temp)
		temp=hashlib.md5(temp.encode()).hexdigest()
		list.append(temp)
		count=count+1
		print('\n')
	elif choice=='3':
		save=input("WHICH TYPE YOU WANT TO SAVE THAT WORD INTO HASH : \n1.SHA256 \t\t\t2.MD5\n[+] : ")
		if save=='1':
			raw.append(temp)
			temp=hashlib.sha256(temp.encode()).hexdigest()
			list.append(temp)
			count=count+1
			print('\n')
		if save=='2':
			raw.append(temp)
			temp=hashlib.md5(temp.encode()).hexdigest()
			list.append(temp)
			count=count+1
			print('\n')
		else:
			print("Unknown command , displaying the stored hashes :--\n")
			os.system('clear')
			break
	elif choice=='4':
		break
		os.system('clear')
	elif choice=='5':
		exit(0)
	else:
		print("Hash No. Not Found , Invalid Option .")


print("\n_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–_–\n")

x=1
print("                          OUTPUT :\n                          ↓↓↓↓↓↓↓↓↓")
while(x<=count):
	print(raw[x],"→→→↓↓↓↓↓↓↓\n>> ",list[x])
	x=x+1
	print('\n')