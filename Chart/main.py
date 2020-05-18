def readStars():
    file = open('Datos/stars.txt', 'r')
    stars = []
    i = 0
    for line in file.readlines():
        stars.append(line.split(" ", 6))
        stars[i][-1] = stars[i][-1].strip('\n')
        if len(stars[i]) > 6:
            temp_string = str(stars[i][6])
            stars[i].pop(6)
            temp_string = temp_string.split("; ")
            stars[i].append(temp_string)
        i += 1

    file.close()


def readConstelation(file):
    const = []
    i = 0
    for line in file.readlines():
        const.append(line.split(","))
        const[i][-1] = const[i][-1].strip('\n')
        i += 1

    file.close()
    return const


def find_constellation(name):
    names = ['boyero', 'casiopea', 'cazo', 'cygnet', 'geminis', 'hydra', 'osamayor', 'osamenor']
    files = [open('Datos/Constelaciones/Boyero.txt', 'r'), open('Datos/Constelaciones/Casiopea.txt', 'r'),
             open('Datos/Constelaciones/Cazo.txt', 'r'), open('Datos/Constelaciones/Cygnet.txt', 'r'),
             open('Datos/Constelaciones/Geminis.txt', 'r'), open('Datos/Constelaciones/Hydra.txt', 'r'),
             open('Datos/Constelaciones/OsaMayor.txt', 'r'), open('Datos/Constelaciones/OsaMenor.txt', 'r')]
    name = name.lower()
    if name in names:
        return readConstelation(files[names.index(name)]), files[names.index(name)].close()
    else:
        return -1


def cart_to_pixel(xCoord, yCoord, size):
    pass


if __name__ == '__main__':
    readStars()
    name = "boyero"
    const = find_constellation(name)
    print(const) if const != -1 else print('No se econtró el nombre de la constelación.')
