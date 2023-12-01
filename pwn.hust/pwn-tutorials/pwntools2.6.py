from pwn import *

p = process('/challenge/pwntools-tutorials-level2.6')

payload = asm('''
    mov rbx,1;
loop:
    add rax,rbx;
    inc rbx;
    cmp rbx,rcx;
    jg done;
    jmp loop;
done:

''',arch='amd64')

p.send(payload)

flag = p.recvall()

print(flag.decode('utf-8'))