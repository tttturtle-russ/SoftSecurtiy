from pwn import *

context(arch='amd64',os='linux',log_level='debug')


p = process('/challenge/pwntools-tutorials-level2.0')

paylaod = asm('mov rax,0x12345678',arch='amd64',os='linux')

p.sendafter('Please give me your assembly in bytes (up to 0x1000 bytes): \n',paylaod)

flag = p.recvall()

print(flag.decode('utf-8'))