# Video Frame Segmentation
:movie_camera: Este projeto trata da segmentação de frames de vídeos, baseando-se em uma análise de histograma.

<p align="center">
 <a href="#Como funciona">Como Funciona?</a> •
 <a href="#Arquivos necessarios">Arquivos necessários</a> • 
 <a href="#Documentacao">Documentação</a> • 
</p>

:question: Como Funciona?
Utilizando as bibliotecas disponíveis para Python , moviepy e Pillow, é extraído um frame específico de um vídeo. Esta imagem(frame) passa por uma função que constrói seu histograma analisando a intensidade de seus pixels, logo após isso outra função analisa qual é o valor máximo de intensidade dos pixels e o envia para a função que definitivamente realiza a segmentação. Utilizando este valor máximo, a função de segmentação compara todos os pixels da imagem a ele: se o valor do pixel for maior, recebe 255(Branco), se for menor recebe 0(Preto); desta forma a imagem proveniente do frame é transformada em uma imagem binária, utilizando o histograma.

:exclamation: Importante: Este projeto adota o padrão RGB.


:floppy_disk: Arquivos necessários

Para executar este projeto é necessário utilizar um vídeo em formato .mp4, anexando à pasta raiz do projeto. O vídeo bigbuckbunny.mp4 está disponível para ser usad de teste no arquivo bigbuckbunny.zip .

:clipboard: Documentação:

https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html
https://pypi.org/project/moviepy/
https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.html
https://numpy.org/
https://pypi.org/project/Pillow/
https://numpy.org/doc/stable/reference/generated/numpy.argmax.html

