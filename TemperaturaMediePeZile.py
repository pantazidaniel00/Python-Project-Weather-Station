from collections import defaultdict

tempzi = defaultdict(list)
ZiuaDeAzi = 0
total =0
c = 0
with open("rezultate_bmp.txt", 'r') as f:
    for line in f:
        if line[:4] == 'data':
            ZiuaDeAzi = line.split()[2]
        elif 'Temperature' in line:
            temp = float(line.split()[1])
            total += temp
            c += 1
            tempzi[ZiuaDeAzi].append(temp)
for day, temps in tempzi.items():
    medie = sum(temps) / len(temps)
    print(f'temperatura medie in ziua {day} este {medie:.2f}')