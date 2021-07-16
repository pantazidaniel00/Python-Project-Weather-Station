import matplotlib.pyplot as plt
import numpy as np

def temperatura():
    with open("rezultate_bmp.txt", 'r') as f:
        temps = []
        for line in f:
            if "Temperature" not in line: continue
            temp = line.split(" ")[1]
            temps.append(temp)
    return temps

def altitudine():
    with open("rezultate_bmp.txt", 'r') as f:
        alti = []
        for line in f:
            if "Altitude" not in line: continue
            altitudine = line.split(" ")[4]
            alti.append(altitudine)
    return alti

y1 = altitudine()
plt.xlabel("Altitudine")
plt.ylabel("Nr_masuratori")
list = []
for i in y1:
    list.append(float(i))
x1 = np.arange(len(y1))
plt.bar(list,x1)
plt.show()


y2 = temperatura()
plt.xlabel("Temperatura")
plt.ylabel("Nr_masuratori")
list1 = []
for i in y2:
    list1.append(float(i))
x2 = np.arange(len(y2))
plt.bar(list1,x2)
plt.show()
