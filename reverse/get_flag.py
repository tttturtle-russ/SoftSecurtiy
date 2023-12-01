#! /usr/bin/python3
from angrmanagement.utils import is_printable
from pwn import *
from z3 import *
from itertools import product

table = [0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0x71,
         0x77, 0x65, 0x72, 0x74, 0x79, 0x75, 0x69, 0x6F, 0x70, 0x61, 0x73,
         0x64, 0x66, 0x67, 0x68, 0x6A, 0x6B, 0x6C, 0x7A, 0x78, 0x63, 0x76,
         0x62, 0x6E, 0x6D, 0x51, 0x57, 0x45, 0x52, 0x54, 0x59, 0x55, 0x49,
         0x4F, 0x50, 0x41, 0x53, 0x44, 0x46, 0x48, 0x4A, 0x4B, 0x4C, 0x5A,
         0x58, 0x43, 0x56, 0x42, 0x4E, 0x4D, 0x2D, 0x2B, 0x2F]
first = 'DiQJ'
second_cipher = 'xw0t'
third_cipher = 'pL97'
forth_cipher = 'eccfb519'
alphaBet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_second():
    result = ''
    second = [i for i in range(0, 4)]
    second_index = [i for i in range(0, 4)]
    for e in range(0, 4):
        second_index[e] = table.index(ord(second_cipher[e]))
    second[0] = (second_index[0] << 2)
    for i in range(1, 4):
        second[i] = (((second[i - 1] >> 2) ^ second_index[i]) << 2)
    for i in range(0, 4):
        result += chr(second[i])
    return result


def get_third():
    t1, t2, t3, t4 = BitVecs('t1 t2 t3 t4', 8)
    solver = Solver()
    solver.add(19 == (t1 >> 2) & 0x3f)
    solver.add(53 == (t2 >> 4) & 0x3f | (16 * t1) & 0x30)
    solver.add(8 == (t3 >> 6) & 3 | (t2 << 2) & 0x3c)
    solver.add(6 == t4 ^ t3 & 0x3f)
    ok = solver.check()
    if ok == sat:
        model = solver.model()
        # 如果字符可见，转义成字符，如果不可见当做数字处理,并拼接成字符串
        result = ''
        for i in [model[t1], model[t2], model[t3], model[t4]]:
            if is_printable(i.as_long()):
                result += chr(i.as_long())
            else:
                result += str(i.as_long())

        return result
    else:
        return 'error'


def get_forth():
    for i in product(alphaBet, repeat=4):
        md5 = hashlib.md5()
        md5.update(''.join(i).encode('utf-8'))
        if md5.hexdigest()[24:32] == forth_cipher:
            return ''.join(i)


license = '{}-{}-{}-{}'.format(first, get_second(), get_third(), get_forth())
print(license)