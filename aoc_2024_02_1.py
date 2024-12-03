"""Advent Of Code 2024 - day 2 puzzle 1
   lines of quantised reports, safe if acc or dec at distances 1..3 """
import fileinput

res=0
with (fileinput.input(files="input/input_02.txt", encoding="utf-8") as f):
    for line in f:
        values = [int(s) for s in line.split()]
        dist_min = 0
        dist_max = 0
        dist = 0
        for idx in range(len(values)-1):
            dist = values[idx] - values[idx+1]
            if 0 == dist: break
            if abs(dist) > 3:
                dist = 0
                break
            if dist < dist_min: dist_min = dist
            if dist > dist_max: dist_max = dist
        safe = (dist != 0) and ( (dist_min <= 0 and dist_max <= 0) or (dist_min >= 0 and dist_max >= 0))
        if safe: res += 1
print(res)