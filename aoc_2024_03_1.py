"""Advent Of Code 2024 - day 1 puzzle 1
   corrupted code, summ all products mul(v1, v1) """
#sample 161 (2*4 + 5*5 + 11*8 + 8*5)
import fileinput, re

res=0
with fileinput.input(files="input/input_03_sample.txt", encoding="utf-8") as f:
    for line in f:
        for cmd in re.findall(r"mul\(\d+\,\d+\)", line):
            cmd_mul = re.split(r'[,)(]', cmd)
            if 'mul' == cmd_mul[0]: res += int(cmd_mul[1])*int(cmd_mul[2])
print(res)