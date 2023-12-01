from pwn import *

p = process('/challenge/pwntools-tutorials-level2.4')

payload = asm('pop rax;sub rax,rbx;push rax',arch='amd64')

p.send(payload)

flag = p.recvall()

print(flag.decode('utf-8'))