import cv2
import numpy as np
import copy

from rgb2gray import rgb2grey
from tookRGBPix import tookRBGPix

medianListBlue = []
medianListGreen = []
medianListRed = []

endereco = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/Images/1.bmp"

# print(endereco[134:-4])
# numero = int(endereco[134:-4])
# print(numero)

#imgDenoised = np.full((724, 724, 3), 0)

#for numImage in range(1,101):
# endereco = enderecoAux + str(numImage) + ".bmp"
# print(endereco)

img = cv2.imread(endereco)
width, height, channels = img.shape
imgEdge = np.full((height+4,width+4,3), 255)

conteudo = img[0:height, 0:width]

height, width, channels = imgEdge.shape
imgEdge[2:height-2, 2:width-2] = conteudo
imgAux = copy.copy(imgEdge)

#consideramos um ruído, uma variável randomica que possui média zero.
#p = p0 + n => p0 é o pixel original e n é o ruído, logo se fizemos a média de N imagens desse pixel
#vamos obter p = p0 + n => p = p0
#usarei um filtro de mediana
#720/3 = 240 não irei usar padding

for i in range(2,width-2):
    for j in range(2,height-2):
        medianListBlue = tookRBGPix(imgAux, i, j, 0)
        medianListGreen = tookRBGPix(imgAux, i, j, 1)
        medianListRed = tookRBGPix(imgAux, i, j, 2)
        medianListBlue.sort()
        medianListGreen.sort()
        medianListRed.sort()
        imgAux[i, j, 0] = medianListBlue[4]
        imgAux[i, j, 1] = medianListGreen[4]
        imgAux[i, j, 2] = medianListRed[4]
cv2.imwrite("imgAux.bmp", imgAux[2:height-2, 2:width-2])

# for i in range(2,width-2):
#     for j in range(2,height-2):
#         imgDenoised[i, j, 0] += imgAux[i, j, 0] / 100
#         imgDenoised[i, j, 1] += imgAux[i, j, 1] / 100
#         imgDenoised[i, j, 2] += imgAux[i, j, 2] / 100
#componentes Y Cr Cb corrompidos pelo Gauss Noise. aplicar uma convolução para resolver isso antes de tudo.
# cv2.imshow(endereco, img)
# cv2.waitKey(0)


    # algum erro quando eu não uso a img no argumento de cvtColor
    # imgAux2 = cv2.imread("/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/imgAux.bmp")
    # imgYCC = cv2.cvtCol1or(imgAux2, cv2.COLOR_BGR2YCR_CB)
    # cv2.imwrite("imgYCC.bmp", imgYCC)

#primeiro separar em Y Cb Cr