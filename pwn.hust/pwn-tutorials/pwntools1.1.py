from pwn import *

context(arch='amd64',os='linux',log_level='debug')

elf = ELF('/challenge/pwntools-tutorials-level1.1')

p = process(elf.path)

payload = b'p\x15'+ p32(123456789,endian='little') + b'Bypass Me:)'

p.sendlineafter("This challenge will leverage pwntools to bypass some conditions, and then print the flag if successful\n",payload)

flag = p.recvline()

print(f'flag is {flag}')