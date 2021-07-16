def temperatura():
    print("Temperatura medie este:")
    total = 0.0
    c = 0
    with open("rezultate_bmp.txt", 'r') as f:
        for line in f:
            if "Temperature" not in line: continue
            temp = line.split(" ")[1]
            total =total+ float(temp)
            c =c+ 1
    print(total / c)
    

def presiune():
    print("Presiunea medie este:")
    total = 0.0
    c = 0
    with open("rezultate_bmp.txt", 'r') as f:
        for line in f:
            if "Pressure" not in line: continue
            presiune = line.split(" ")[4]
            total =total+ float(presiune)
            c =c+ 1
    print(total / c)

def altitudine():
    print("Altitudinea medie este:")
    total = 0.0
    c = 0
    with open("rezultate_bmp.txt", 'r') as f:
        for line in f:
            if "Altitude" not in line: continue
            altitudine = line.split(" ")[4]
            total =total+ float(altitudine)
            c =c+ 1
    print(total / c)
temperatura()
presiune()
altitudine()