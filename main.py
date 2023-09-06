from resultantes import resultantes
from convertir import convert


def main_resultante():
    v1 = []
    v2 = []

    # vector 1
    x1 = float(input('Ingrese el valor de x1: '))
    y1 = float(input('Ingrese el valor de y1: '))
    z1 = float(input('Ingrese el valor de z1: '))

    v1.append(x1)
    v1.append(y1)
    v1.append(z1)

    # vector 2
    x2 = float(input('Ingrese el valor de x2: '))
    y2 = float(input('Ingrese el valor de y2: '))
    z2 = float(input('Ingrese el valor de z2: '))
    v2.append(x2)
    v2.append(y2)
    v2.append(z2)

    resultantes(v1, v2)


def main():

    # v1 = [4, 5, -7]
    # v2 = [3, 2, 8]

    main_resultante()
    convert()


if __name__ == '__main__':
    main()
