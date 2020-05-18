
import numpy as np
import cv2


stars = []
img = np.zeros((1000, 1000, 3), dtype=np.uint8)


def readStars():
    file = open('Datos/stars.txt', 'r')
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


def readConstellation(file):
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
        return readConstellation(files[names.index(name)]), files[names.index(name)].close()
    else:
        return -1


def cart_to_pixel(xCoord, yCoord):
    return int(500*(xCoord + 1)), int(500*(1 - yCoord))


def drawStars():
    for star in stars:
        star_size = round(10 / (float(star[4]) + 2))
        x = float(star[0])
        y = float(star[1])

        x, y = cart_to_pixel(x, y)
        cv2.rectangle(img, (x, y), (x, y), (255, 255, 255), star_size)


def drawConstellations(consts):
    i = 0
    while i < len(const[0]):
        j = 0
        pos = []
        while j < 2:
            for star in stars:
                if len(star) > 6:
                    if len(star[6]) == 1:
                        if const[0][i][j] == star[6][0]:
                            pos.append(star[0])
                            pos.append(star[1])
                    else:
                        if const[0][i][j] == star[6][0] or const[0][i][j] == star[6][1]:
                            pos.append(star[0])
                            pos.append(star[1])
            j += 1
        x, y = cart_to_pixel(float(pos[0]), float(pos[1]))
        x1, y1 = cart_to_pixel(float(pos[2]), float(pos[3]))
        cv2.line(img, (x, y), (x1, y1), (0, 255, 255), 1)
        i += 1


if __name__ == '__main__':
    readStars()
    drawStars()
    names = ['boyero', 'casiopea', 'cazo', 'cygnet', 'geminis', 'hydra', 'osamayor', 'osamenor']
    for name in names:
        try:
            const = find_constellation(name)
            drawConstellations(const) if const != -1 else print('No se econtró el nombre de la constelación.')
        except Exception as e:
            print("F")
    # rot = cv2.getRotationMatrix2D((500, 500), 180, 1.0)
    # rot = cv2.warpAffine(img, rot, (1000, 1000))
    cv2.imwrite("space.png", img)

