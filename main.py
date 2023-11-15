import numpy as np
import matplotlib.pyplot as plt

#Ingreso de datos iniciales y cálculo de ecuación de la recta
user = float(input('Ingresa el valor de reflujo interno en zona de rectificación: \n'))
xd = float(input('Ingresa el valor de fracción molar de tope: \n'))
xb = float(input('Ingresa el valor de fracción molar de fondo/residuo: \n'))
zf = float(input('Ingresa el valor de fracción molar de alimentacion: \n'))
#alpha = float(input('Ingresa el valor de alpha: \n'))
q = float(input('Ingresa el valor de q, de acuerdo al estado físico-técnico de la alimentacion: \n'))

while float(user) <= 0 or float(xd) <= 0 or float(xb) <= 0:
    user = float(input("Ingresa el valor de reflujo externo: \n"))
    xd = float(input("Ingresa el valor de fracción molar de tope: \n"))
    xb = float(input("Ingresa el valor de fracción molar de fondo/residuo: \n"))
    zf = float(input('Ingresa el valor de fracción molar de alimentacion: \n'))

R = float(user/0.4)
y = float(R/(R+1))
y_1 = float(xd/(R+1))
alpha = R + 1
print('La ecuación de la recta es: ')
print(str(y)+"x + "+str(y_1))
# Initialization and calculation of equilibrium curve

y = np.arange(0, 1.1, 0.1)
ye = y
xe = ye / (alpha + (1 - alpha) * ye)
xq = ((R + 1) * zf + (q - 1) * xd) / (R + q)
yq = (R * zf + q * xd) / (R + q)

plt.plot(xe, ye, 'r')
plt.plot([0, 1], [0, 1], color=[0, 0, 0])
plt.plot([xd, xq], [xd, yq], color=[1, 0, 1])
plt.plot([zf, xq], [zf, yq], color=[1, 0, 1])
plt.plot([xb, xq], [xb, yq], color=[1, 0, 1])

    # Rectifying section
i = 1
xop = [xd]
yop = [xd]
y = xd

while xop[i - 1] > xq:
    xop.append(y / (alpha + (1 - alpha) * y))
    yop.append(R * xop[i] / (R + 1) + xd / (R + 1))

    # Rectifying operating line
    y = yop[i]
    plt.plot([xop[i - 1], xop[i]], [yop[i - 1], yop[i]], color=[0, 0, 1])

    if xop[i] > xq:
        plt.plot([xop[i - 1], xop[i]], [yop[i-1], yop[i-1]], color=[0, 0, 1])
        plt.plot([xop[i], xop[i]], [yop[i - 1], yop[i]], color=[0, 0, 1])

    i += 1

feedn = i - 1

# Stripping section
c1 = (yq - xb) / (xq - xb)
c2 = (yq - xq) / (xq - xb)

yop[i - 1] = c1 * xop[i - 1] - c2 * xb
y = yop[i - 1]

plt.plot([xop[i - 2], xop[i-1]], [yop[i - 2], yop[i - 2]], color=[0, 0, 1])

plt.plot([xop[i - 1], xop[i - 1]], [yop[i - 2], yop[i - 1]], color=[0, 0, 1])

while xop[i - 1] > xb:
    xop.append(y / (alpha + (1 - alpha) * y))
    yop.append(c1 * xop[i] - c2 * xb)
    y = yop[i]

    plt.plot([xop[i - 1], xop[i]], [yop[i - 1], yop[i]], color=[0, 0, 1])

    if xop[i] > xb:
        plt.plot([xop[i - 1], xop[i]], [yop[i-1], yop[i-1]], color=[0, 0, 1])
        plt.plot([xop[i], xop[i]], [yop[i - 1], yop[i]], color=[0, 0, 1])

    i += 1

plt.plot([xop[i - 2], xop[i-1]], [yop[i - 2], yop[i - 2]], color=[0, 0, 1])

plt.plot([xop[i - 1], xop[i - 1]], [yop[i - 2], yop[i - 1]], color=[0, 0, 1])

plt.xlabel('x')
plt.ylabel('y')

totaln = i - 1

print('Etapas teóricas =', totaln)
print('Número de Platos teóricos =', totaln-2)
print('Plato de Alimentación =', feedn)

plt.show()
