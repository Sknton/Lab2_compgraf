import matplotlib.pyplot as plt
from sympy import true

plt.figure(figsize=(10,5.625))

f = open('DS1.txt', 'r')
x_list =[]
y_list = []
while true:
    x = f.read(3)
    if x!='':
        f.read(1)
        y = f.read(3)
        f.read(1)
        x_list.append(int(x))
        y_list.append(int(y))
    else:
        break
plt.scatter(x_list, y_list, c ="red", s = 1)
plt.show()
f.close

