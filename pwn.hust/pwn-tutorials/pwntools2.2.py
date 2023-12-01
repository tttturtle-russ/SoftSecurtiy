from pwn import *

p = process('/challenge/pwntools-tutorials-level2.2')

payload = asm('idiv rbx;mov rax,rdx;add rax,rcx;sub rax,rsi;',arch='amd64',os='linux')

p.send(payload)

flag = p.recvall()

print(flag.decode('utf-8'))