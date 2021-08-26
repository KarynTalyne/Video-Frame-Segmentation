import moviepy.editor as mpe
import matplotlib.pyplot as plt
import numpy as np


# A biblioteca moviepy,pode ser instalada através do comando pip install moviepy no prompt de comando ou Anaconda Prompt


def max_index_fast(array):  # função que localiza o nível de cinza correspondente ao maior pico do histograma
    indice = np.argmax(array)  # é obtido o índice do maior pico do histograma através da função argmax
    p = np.unravel_index(indice, array.shape)  # converte um índice em uma tupla de matrizes de coordenadas.
    t = p[0]  # é obtido o valor do nível de cinza
    return t  # retorna o valor para a função histogram_analysis


def threshold(img, thresh):  # função que realiza o threshold

    if thresh > 200:
        threshold = thresh / 2  # se thresh é maior que 200,o valor é divido para evitar um valor de threshold muito alto
        # print('\n',thresh,'\n')
    else:
        threshold = thresh
    (l, c, p) = img.shape
    binary = np.zeros(shape=(l, c),
                      dtype=np.uint8)  # uma matriz preenchida com zeros é criada para receber a imagem binária
    for i in range(l):
        for j in range(c):
            # cada pixel da imagem é comparado com o valor do threshold
            r, g, b = img[i, j]
            lightness = (float(min(r, g, b)) + float(max(r, g, b))) / 2
            # se o valor do pixel for maior, ele recebe o valor 255(branco)
            if lightness > threshold:
                binary[i, j] = 255
            # se o valor for menor recebe 0(preto)
            else:
                binary[i, j] = 0
    return binary  # a imagem binária é retornada


def histogram(img):  # função que faz o histograma
    (l, c, p) = img.shape  # são obtidas os valores das dimensões da matriz da imagem
    # A imagem é convertida em escala de cinza
    img_gray = ((0.2126 * img[:, :, 0]) + (0.7152 * img[:, :, 1]) + (0.0722 * img[:, :, 2])).astype(np.uint8)
    histogram = np.zeros(256, dtype=np.int32)  # Uma matriz preenchida com zeros é criada para receber o histograma

    for i in range(l):
        for j in range(c):
            intensity = img_gray[i, j]  # a intensidade de cada pixel,seu valor na escala de cinza
            histogram[intensity] += 1  # o histograma computa quantos pixels possuem esta intensidade

    # mostra o gráfico do histograma
    '''
    print('\n')
    plt.subplot(2, 1, 2)
    plt.bar(range(256), histogram)
    print('\n')
    '''
    return histogram  # retorna o histograma


def histogram_analysis(img_0):  # função que analisa o histograma e faz a segmentação

    h = histogram(img_0)  # é feito histograma do frame
    v = max_index_fast(h)  # o histograma é enviado para a função que vai obter o valor para threshold
    img_f = threshold(img_0, v)  # com o valor do threshold obtido,a imagem é transformada em binária
    return img_f  # a imagem processada é retornada


def Open_and_informer(name):  # função de interface,obtêm as informações do vídeo
    video = mpe.VideoFileClip(name)  # Abre o vídeo submetido
    d = video.duration  # Obtêm a duração do vídeo

    return d, video  # retorna a duração e o vídeo


def Extract(video, time):  # função que extrai o frame do vídeo
    img_in = video.get_frame(time)[:, :, :3]  # a imagem referente ao segundo(tempo) escolhido é extraída
    img_out = histogram_analysis(img_in)  # a imagem é enviada para a análise do histograma

    return img_out, img_in  # A imagem original e a imagem processada são retornadas


'''
Interface construída para explicação, pode ser retirada caso este algoritmo seja anexado a outro, de forma
que este conheça as informações utilizadas do vídeo a ser submetido.

'''
'''
name = input('Qual o nome do vídeo a ser acessado?\n\n')
(resp1,v)=Open_and_informer(name) # é chamada a função inicial, e esta retorna a duração do vídeo e o vídeo
print('A duração do vídeo é de', resp1, 'segundos\n')
time = input('Insira o tempo em segundos, referente ao frame desejado:\n')# é obtido o instante de tempo para extrair o frame
print('\n')
(out,entry) = Extract(v,time)# é chamada a função de extração e a segmentação é iniciada,e é retornada a imagem processada
# são printadas a imagem original e a imagem processada
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
print('1-Imagem original:\n')
plt.imshow(entry)
print('2-Imagem processada:\n')
plt.subplot(2, 1, 2)
plt.imshow(out,cmap="gray")

'''
# teste feito com o vídeo bigbuckbunny.mp4

print('Qual o nome do vídeo a ser acessado?\n\n')
# abrindo um vídeo de 5 segundos
name = "bigbuckbunny.mp4"
(resp1, v) = Open_and_informer(name)
print('A duração do vídeo é de', resp1, 'segundos\n')
# selecionando o frame do segundo 4
time = 4
print('\n')
# Chamando a função que inicia a segmentação
'''
É chamada a função de extração e a segmentação é iniciada,e é retornada a imagem processada
'''
(out, entry) = Extract(v, time)
# Mostrando os resultados
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
print('1-Imagem original:\n')
plt.imshow(entry)
print('2-Imagem processada:\n')
plt.subplot(2, 1, 2)
plt.imshow(out, cmap="gray")
