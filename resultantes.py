import math


def resultantes(v1, v2):
    vector1 = input('Ingrese el nombre del vector 1: ')
    vector2 = input('Ingrese el nombre del vector 2: ')

    max_value = max(v1[0], v1[1], v1[2], v2[0], v2[1], v2[2])

    # calcular vector resultante
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    z = v1[2] + v2[2]
    v = [x, y, z]

    # procedimiento
    print('\n')
    print(
        f'El vector resultante es: ({v1[0]}) + ({v2[0]})i + ({v1[1]}) + ({v2[1]})j + ({v1[2]}) + ({v2[2]})k')
    print(
        f'El vector resultante es: ({v1[0] + v2[0]})i + ({v1[1] + v2[1]})j + ({v1[2] + v2[2]})k')
    print(f'El vector resultante es: ({x})i + ({y})j + ({z})k')
    print(f'El vector resultante es: {v}')

    # calcular modulo del vector resultante
    modulo = (x**2 + y**2 + z**2)**0.5

    # procedimiento
    print('\n')
    print(f'El modulo del vector resultante es: √({x})² + ({y})² + ({z})²')
    print(
        f'El modulo del vector resultante es: √({x**2}) + ({y**2}) + ({z**2})')
    print(f'El modulo del vector resultante es: √({x**2 + y**2 + z**2})')
    print(f'El modulo del vector resultante es: {modulo}')

    # calcular angulo entre el vector resultante y el eje x
    theta = math.atan(y/x)
    angulo = math.degrees(theta)

    # procedimiento
    print('\n')
    print(f'El angulo entre el vector resultante y el eje x es: atan({y}/{x})')
    print(f'El angulo entre el vector resultante y el eje x es: atan({y/x})')
    print(f'El angulo entre el vector resultante y el eje x es: {angulo}°')

    # calcular angulo entre el vector resultante y el eje z
    phi = math.atan(z/(x**2 + y**2)**0.5)
    angulo2 = math.degrees(phi)

    # mostrar el modulo del vector resultante
    print('\n')
    print(f'El modulo del vector resultante es: {modulo}')

    # mostrar el angulo entre el vector resultante y el eje x
    print('\n')
    print(f'El angulo entre el vector resultante y el eje x es: {angulo}°')

    # mostrar el angulo entre el vector resultante y el eje z
    print('\n')
    print(f'El angulo entre el vector resultante y el eje z es: {angulo2}°')

    # graficar los 3 vectores
    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # hacer mas grande x, y, z en el grafico

    ax.set_xlim(-max_value, max_value)
    ax.set_ylim(-max_value, max_value)
    ax.set_zlim(-max_value, max_value)

    # graficar punto
    ax.scatter(x, y, z, color='k')

    # graficar el vector
    # ax.quiver(0, 0, 0, x, y, z, color='r')

    # hacer el vector resultante mas lindo
    ax.quiver(0, 0, 0, x, y, z, color='r', arrow_length_ratio=0.1)

    # graficar el vector 1
    ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='b', arrow_length_ratio=0.1)
    ax.text(x, y, z, f'R = ({x}, {y}, {z})', color='r')

    # agregar flecha al vector 1 y label que diga vector 1 y sus coordenadas
    ax.quiver(v1[0], v1[1], v1[2], 0, 0, 0, color='b', arrow_length_ratio=0.1)
    ax.text(v1[0], v1[1], v1[2],
            f'{vector1} ( {v1[0]}, {v1[1]}, {v2[2]} ) ', color='b')

    # graficar el vector 2
    ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g', arrow_length_ratio=0.1)

    # agregar flecha al vector 2 y label que diga vector 2 y sus coordenadas
    ax.quiver(v2[0], v2[1], v2[2], 0, 0, 0, color='g', arrow_length_ratio=0.1)
    ax.text(v2[0], v2[1], v2[2],
            f'{vector2} ( {v2[0]}, {v2[1]}, {v2[2]} )', color='g')

    # mostrar grafica
    plt.show()
