import math

#promien = input("podaj promien kola")
promien = 5

pole = math.pi * int(promien)**2

print(pole)

for i in range(1,1000):
    g = ""
    for x in range(int((math.sin(i/5)+1.33)*10)):
        g += " "
    print(g + "( ͡° ͜ʖ ͡°)")