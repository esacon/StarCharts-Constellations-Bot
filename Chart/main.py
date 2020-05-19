
import numpy as np
import cv2

stars = []
names = ['boyero', 'casiopea', 'cazo', 'cygnet', 'geminis', 'hydra', 'osamayor', 'osamenor']
img = np.zeros((1000, 1000, 3), dtype=np.uint8)  # Establece una imagen como una matriz


# Recorre el archivo 'stars.txt' y separa los datos del mismo para almacenarlo en una lista
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


# Recibe un archivo de constelaciones y separa sus datos en un arreglo
def readConstellation(file):
    const = []
    i = 0
    for line in file.readlines():
        const.append(line.split(","))
        const[i][-1] = const[i][-1].strip('\n')
        i += 1

    file.close()
    return const


# Recibe un parámetro nombre y selecciona el archivo correspondiente
def find_constellation(name):
    files = [open('Datos/Constelaciones/Boyero.txt', 'r'), open('Datos/Constelaciones/Casiopea.txt', 'r'),
             open('Datos/Constelaciones/Cazo.txt', 'r'), open('Datos/Constelaciones/Cygnet.txt', 'r'),
             open('Datos/Constelaciones/Geminis.txt', 'r'), open('Datos/Constelaciones/Hydra.txt', 'r'),
             open('Datos/Constelaciones/OsaMayor.txt', 'r'), open('Datos/Constelaciones/OsaMenor.txt', 'r')]
    name = name.lower()
    if name in names:
        return readConstellation(files[names.index(name)]), files[names.index(name)].close()
    else:
        return -1


# Convierte las coordenadas cartesianas a pixeles para manipular la imagen de mejor manera
def cart_to_pixel(xCoord, yCoord):
    return int(500*(xCoord + 1)), int(500*(1 - yCoord))


# Dibuja las estrellas en una imagen vacía de fondo negro
def drawStars():
    for star in stars:
        star_size = round(10 / (float(star[4]) + 2))
        x = float(star[0])
        y = float(star[1])

        x, y = cart_to_pixel(x, y)
        cv2.rectangle(img, (x, y), (x, y), (255, 255, 255), star_size)

    cv2.imwrite("Images/stars.png", img)


# Se encarga de dibujar una constelación que recibe como parámetro
def drawConstellations(const, color, img2):
    i = 0
    while i < len(const[0]):
        j = 0
        pos = []
        while j < 2:
            for star in stars:
                # Valida que la estrella esociga cuente con el parámetro nombre
                if len(star) > 6:
                    # Compara el nombre dentro de cada constelación con cada nombre posible para una estrella
                    if len(star[6]) == 1:
                        if const[0][i][j] == star[6][0]:
                            pos.append(star[0])
                            pos.append(star[1])
                    else:
                        if const[0][i][j] == star[6][0] or const[0][i][j] == star[6][1]:
                            pos.append(star[0])
                            pos.append(star[1])
                        if len(star[6]) > 2:
                            if const[0][i][j] == star[6][2]:
                                pos.append(star[0])
                                pos.append(star[1])
            j += 1
        x, y = cart_to_pixel(float(pos[0]), float(pos[1]))
        x1, y1 = cart_to_pixel(float(pos[2]), float(pos[3]))
        cv2.line(img2, (x, y), (x1, y1), color, 1)
        # En caso que varias estrellas tengan un mismo nombre, se grafica también la conexión entre ambos puntos
        if len(pos) > 4:
            x2, y2 = cart_to_pixel(float(pos[4]), float(pos[5]))
            cv2.line(img2, (x1, y1), (x2, y2), color, 1)
        i += 1


# Grafica cada constelación de un color distinto
def drawAllConst():
    color = [(0, 255, 255), (255, 0, 255), (255, 255, 0), (0, 255, 0), (0, 0, 255), (34, 126, 230), (7, 182, 23),
             (254, 19, 188)]
    names = ['boyero', 'casiopea', 'cygnet', 'geminis', 'hydra', 'osamayor', 'osamenor', 'cazo']
    i = 0
    for name in names:
        const = find_constellation(name)
        drawConstellations(const, color[i], img)
        i += 1

    cv2.imwrite("Images/space.png", img)


# Genera un archivo .png para cada constelación
def generateConst():
    for name in names:
        img2 = np.copy(img)
        drawConstellations(find_constellation(name), (0, 255, 255), img2)
        const_name = "Images/" + name.lower() + ".png"
        cv2.imwrite(const_name, img2)


if __name__ == '__main__':
    readStars()
    drawStars()
    generateConst()
    drawAllConst()

