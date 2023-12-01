from pwn import *

p = process('/challenge/pwntools-tutorials-level2.3')

payload = asm('mov rsi,0x404000;mov rdi,0x405000;mov rcx,0x8;rep movsb',arch='amd64')

p.send(payload)

flag= p.recvall()

print(flag.decode('utf-8'))