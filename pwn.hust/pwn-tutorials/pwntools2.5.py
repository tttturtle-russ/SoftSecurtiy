from pwn import *

p = process('/challenge/pwntools-tutorials-level2.5')

payload = asm('''
    pop rax;
    cmp rax,0;
    jg positive;
    neg rax;
positive:
    push rax;
''',arch='amd64')

p.send(payload)

flag = p.recvall()

print(flag.decode('utf-8'))