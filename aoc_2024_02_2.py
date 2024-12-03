"""Advent Of Code 2024 - day 2 puzzle 1
   lines of quantised reports, safe if acc or dec at distances 1..3
   allow for a single error value in each line"""
import fileinput

res=0
with (fileinput.input(files="input/input_02.txt", encoding="utf-8") as f):
    for line in f:
        values = [int(s) for s in line.split()]
        last = values[0]
        asc = 0 < (values[1] - values[0])
        penalties = 0
        idx = 0
        offs = 0
        skip = 0
        if (last < values[idx+1] and values[idx+1] > values[idx+2]) or \
             (last > values[idx+1] and values[idx+1] < values[idx+2]) or \
             (values[idx + 1] - last == 0) or  \
             (abs(values[idx + 1] - last) > 3):
            print("penalty: ", last, int(values[idx + 1]), values[idx + 2])
            penalties = 1
            last = values[idx] # strip value in the middle
            offs = 1
            asc = (0 < values[idx+2] - last)
        for idx in range(len(values)-offs):
            #print("idx, offs, last, asc:", idx, offs, last, asc)
            if len(values) > idx+offs+1:
                print(idx + offs, ":", last, "<=>", values[idx + 1 + offs], last)
                dist = values[idx + 1 + offs] - last
                lasc = (0 < dist)
                if (not asc == lasc) or dist == 0 or abs(dist) > 3:
                    print("penalty dist:", dist, "asc:", asc, lasc)
                    penalties += 1
                    #offs += 1
                else:
                    last = values[idx + 1 + offs]
            if 1 < penalties:
                break
        safe = (penalties < 2)
        print(values, "safe:", safe, "penalties:", penalties, "asc:", asc, "offs:", offs)
        if safe: res += 1
print(res)