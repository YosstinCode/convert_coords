import math as match
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def cartesianas_a_cilindricas():
    # pedir coordenada en 3 dimensiones y calcular su coordenada cilindrica

    punto = input('Ingrese el nombre del punto: ')

    x = float(input('Ingrese la coordenada x: '))
    y = float(input('Ingrese la coordenada y: '))
    z = float(input('Ingrese la coordenada z: '))
    print("\n")

    # calcular la coordenada cilindrica
    r = (x**2 + y**2)**0.5
    theta = match.atan(y/x)
    angulo = match.degrees(theta)
    h = z

    # procedimiento del calculo de la coordenada cilindrica

    # calcular el radio
    print(f'Radio = √({x})² + ({y})²')
    print(f'Radio = √({x**2}) + ({y**2})')
    print(f'Radio = √({x**2 + y**2})')
    print(f'Radio = {r}')
    print("\n")
    # calcular el angulo
    print(f'Theta = atan({y}/{x})')
    print(f'Theta = atan({y/x})')
    print(f'Theta = {theta}')
    print("\n")

    # angulo en grados
    print(f'Theta = {theta} = {match.degrees(theta)}°')
    print("\n")

    # calcular la altura
    print(f'Altura = Z = {z}')
    print("\n")

    # mostrar la coordenada cilindrica
    print('La coordenada cilindrica es: (', r, ',', angulo, '°,', h, ')')

    return ((x, y, z), r, (theta, angulo), h, punto)


def cartesianas_a_esfericas():

    # pedir coordenada en 3 dimensiones y calcular su coordenada esferica

    punto = input('Ingrese el nombre del punto: ')

    x = float(input('Ingrese la coordenada x: '))
    y = float(input('Ingrese la coordenada y: '))
    z = float(input('Ingrese la coordenada z: '))
    print("\n")

    # calcular la coordenada esferica
    r = (x**2 + y**2 + z**2)**0.5
    theta = match.atan(y/x)
    angulo = match.degrees(theta)
    phi = match.atan((x**2 + y**2)**0.5/z)
    angulo_phi = match.degrees(phi)

    # procedimiento del calculo de la coordenada esferica

    # calcular el radio
    print(f'Radio = √({x})² + ({y})² + ({z})²')
    print(f'Radio = √({x**2}) + ({y**2}) + ({z**2})')
    print(f'Radio = √({x**2 + y**2 + z**2})')
    print(f'Radio = {r}')
    print("\n")

    # calcular el angulo theta
    print(f'Theta = atan({y}/{x})')
    print(f'Theta = atan({y/x})')
    print(f'Theta = {theta}')
    print("\n")

    # angulo theta en grados
    print(f'Theta = {theta} = {match.degrees(theta)}°')
    print("\n")

    # calcular el angulo phi

    print(f'Phi = atan(√({x})² + ({y})² / {z})')
    print(f'Phi = atan(√({x**2}) + ({y**2}) / {z})')
    print(f'Phi = atan(√({x**2 + y**2}) / {z})')
    print(f'Phi = atan({(x**2 + y**2)**0.5} / {z})')
    print(f'Phi = atan({(x**2 + y**2)**0.5/z})')
    print(f'Phi = {phi}')
    print("\n")

    # angulo phi en grados
    print(f'Phi = {phi} = {match.degrees(phi)}°')

    # mostrar la coordenada esferica
    print('La coordenada esferica es: (', r, ',', angulo, '°,', angulo_phi, '° )')
    # mostar la coordenada esferica con angulos en radianes
    print('La coordenada esferica es: (', r, ',', theta, ',', phi, ')')

    return ((x, y, z), r, (theta, angulo), (phi, angulo_phi), punto)


def graficar_cilindrica(x, y, z, r, theta, angulo, h, punto):
    # graficar el vector

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # graficar punto
    ax.scatter(x, y, z, color='k')

    # graficar el vector
    ax.quiver(0, 0, 0, x, y, z, color='r', arrow_length_ratio=0.1)

    max_value = max(x, y, z)

    # ponerle label que diga vector
    ax.text(x, y, z, f'{punto} ( {x}, {y}, {z} )', color='r')

    # # hacer mas grande
    # ax.set_xlim(-max_value, max_value)
    # ax.set_ylim(-max_value, max_value)
    # ax.set_zlim(-max_value, max_value)

    # graficar radio

    theta = np.linspace(0, 2*np.pi, 100)
    theta_degrees = np.linspace(0, 360, 100)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    z = np.zeros(100)
    ax.plot(x, y, z, color='b')

    # agregar linea que indique el radio

    ax.plot([0, r], [0, 0], [0, 0], color='b')

    # ponerle label que diga radio
    ax.text(r, 0, 0, f'  Radio = {round(r, 4)}', color='b')

    # graficar la altura
    x = np.zeros(100)
    y = np.zeros(100)
    z = np.linspace(0, h, 100)
    ax.plot(x, y, z, color='g')

    # ponerle label que diga altura
    ax.text(0, 0, h, f' Altura = {h}', color='g')

    # label con el angulo

    ax.text(r/2, 0, h/2, f'θ = {round(angulo, 3)}°', color='k')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


# def graficar_esferica(x, y, z, r, theta, angulo, phi, angulo_phi, punto):

#     pass

#     # graficar el vector

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     # graficar punto
#     ax.scatter(x, y, z, color='k')

#     # graficar el vector
#     ax.quiver(0, 0, 0, x, y, z, color='r')

#     # ponerle label que diga vector
#     ax.text(x, y, z, f'{punto} ( {x}, {y}, {z} )', color='r')

#     # label con el radio en la mitad del vector

#     ax.text(x/2, y/2, z/2, f'r = {round(r, 4)}', color='r')

#     # circulo en el plano xy

#     theta = np.linspace(0, 2*np.pi, 100)
#     theta_degrees = np.linspace(0, 360, 100)
#     x = r*np.cos(theta)
#     y = r*np.sin(theta)
#     z = np.zeros(100)
#     ax.plot(x, y, z, color='b')

#     # graficar linea sin la altura

#     x = r*np.cos(theta)
#     y = r*np.sin(theta)
#     z = np.zeros(100)

#     ax.plot(x, y, z, color='b')

#     # poner label a la linea sin altura

#     ax.text(r/2, r/2, 0, f'θ = {round(angulo, 3)}°', color='k')

#     # poner label a phi

#     ax.text(r/2, 0, r/2, f'φ = {round(angulo_phi, 3)}°', color='k')

#     # linea que represente el angulo phi por debajo del vector en el plano xy

#     x = r*np.cos(theta)
#     y = r*np.sin(theta)
#     z = np.zeros(100)

#     ax.plot(x, y, z, color='b')

#     x = r*np.cos(theta)
#     y = np.zeros(100)
#     z = r*np.sin(theta)
#     ax.plot(x, y, z, color='b')

#     # mostrar

#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')

#     plt.show()


def cilindrica_a_cartesianas():

    punto = input('Ingrese el nombre del punto: ')

    # pedir datos

    r = float(input('Ingrese el radio: '))
    angulo = float(input('Ingrese el angulo: '))
    h = float(input('Ingrese la altura: '))

    # convertir angulo a radianes

    theta = match.radians(angulo)

    # calcular coordenadas cartesianas

    x = r*np.cos(theta)
    y = r*np.sin(theta)
    z = h

    # procedmiento para calcular

    print(f'x = r*cos(θ) = {r}*cos({angulo}) = {x}')
    print(f'y = r*sin(θ) = {r}*sin({angulo}) = {y}')
    print(f'z = h = {h}')

    # mostrar coordenadas cartesianas

    print('Las coordenadas cartesianas son: (', x, ',', y, ',', z, ')')

    return (x, y, z), r, (theta, angulo), h, punto


def cilindricas_a_esfericas():

    # pedir datos

    r = float(input('Ingrese el radio: '))
    angulo = float(input('Ingrese el angulo: '))
    h = float(input('Ingrese la altura: '))

    # convertir angulo a radianes

    theta = match.radians(angulo)

    # convertir coordenadas cartesianas a esfericas

    r = (r**2 + h**2)**(1/2)
    phi = match.atan(h/r)

    # procedmiento para calcular

    print(f'r = √(x² + y² + z²) = √({r}² + {h}²) = {r}')
    print(f'θ = arctan(y/x) = arctan({h}/{r}) = {theta}')

    # mostrar coordenadas esfericas

    print('Las coordenadas esfericas son: (', r, ',', theta, ',', phi, ')')

    # convertir angulos a grados

    angulo = match.degrees(theta)
    angulo_phi = match.degrees(phi)


def graficar_catersianas(x, y, z, punto):

    # graficar el vector

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # graficar punto
    ax.scatter(x, y, z, color='k')

    # graficar el vector
    ax.quiver(0, 0, 0, x, y, z, color='r')

    # ponerle label que diga vector
    ax.text(x, y, z, f'{punto} ( {x}, {y}, {z} )', color='r')

    # mostrar

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def convert():

    print('1. cartesianas a cilindricas')
    print('2. cartesianas a esfericas')
    print('3. Esfericas a cartesianas')
    print('4. Esfericas a cilindricas')

    opc = input('ingrese opcion: ')

    if opc == '1':
        (x, y, z), r, (theta, angulo), h, punto = cartesianas_a_cilindricas()
        graficar_cilindrica(x, y, z, r, theta, angulo, h, punto)
    elif opc == '2':
        (x, y, z), r, (theta, angulo), (phi,
                                        angulo_phi), punto = cartesianas_a_esfericas()
        # graficar_esferica(x, y, z, r, theta, angulo, phi, angulo_phi, punto)
    elif opc == '3':
        (x, y, z), r, (theta, angulo), h, punto = cilindrica_a_cartesianas()
        graficar_catersianas(x, y, z, punto)
    elif opc == '4':
        cilindricas_a_esfericas()
