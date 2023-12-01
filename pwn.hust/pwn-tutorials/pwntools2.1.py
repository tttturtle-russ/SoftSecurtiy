from pwn import *

p = process('/challenge/pwntools-tutorials-level2.1')

payload = asm('push rax;mov rax,rbx;pop rbx;',arch='amd64',os='linux')

p.send(payload)

flag = p.recvall()

print(flag.decode('utf-8'))