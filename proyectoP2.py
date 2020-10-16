from tkinter import *
from tkinter.filedialog import askopenfilename

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sys 
sys.path.insert(1, 'dsp-modulo')
from thinkdsp import read_wave
import numpy

principal = Tk()
principal.title("Análisis audio")

strDirArchivo = StringVar()
strDirArchivo.set("Dirección del archivo:")

strDireccionArchivo = StringVar()
strDireccionArchivo.set("")

strResultado = StringVar()
strResultado.set("Mensaje decodificado:")

def abrirArchivo():
    global direccionArchivo
    direccionArchivo = askopenfilename()
    strDireccionArchivo.set(direccionArchivo)


def analizarArchivo():
    global direccionArchivo
    texto = ""
    waveTexto = read_wave(direccionArchivo)

    #segmento_waveTexto= waveTexto.segment(0, 0.5)
    #NumLetras = segmento_waveTexto / 100

    #print(NumLetras)
    #print("Inicio: " + str(waveTexto.start))
    #print("Duración: " + str(waveTexto.duration))
    #print("Frecuencia de muestreo: " + str(waveTexto.framerate))

    segmentosNumero = []
    for i in range(6):
        segmentosNumero.append(waveTexto.segment(start=i*0.5, duration=0.5))

    frecuenciasLetrasDTMF = [200, 240, 280, 320, 360, 400, 440, 480, 520, 
    560, 600, 640, 680, 720, 760, 800, 840, 880, 
    920, 6960, 1000, 1040, 1080, 1120, 1160, 1200]

    tolerancia = 10

    for segmento in segmentosNumero:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 199:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        frecuenciaLetra = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciasLetrasDTMF:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    frecuenciaLetra = frecuenciaDTMF 
        if frecuenciaLetra == 200:
            texto = texto + "A"
        elif frecuenciaLetra == 560:
            texto = texto + "B"
        elif frecuenciaLetra == 920:
            texto = texto + "C"
        elif frecuenciaLetra == 240:
            texto = texto + "D"
        elif frecuenciaLetra == 600:
            texto = texto + "E"
        elif frecuenciaLetra == 960:
            texto = texto + "F"
        elif frecuenciaLetra == 280:
            texto = texto + "G"
        elif frecuenciaLetra == 640:
            texto = texto + "H"
        elif frecuenciaLetra == 1000:
            texto = texto + "I"
        elif frecuenciaLetra == 320:
            texto = texto + "J"
        elif frecuenciaLetra == 680:
            texto = texto + "K"
        elif frecuenciaLetra == 1040:
            texto = texto + "L"
        elif frecuenciaLetra == 360:
            texto = texto + "M"
        elif frecuenciaLetra == 720:
            texto = texto + "N"
        elif frecuenciaLetra == 1080:
            texto = texto + "O"
        elif frecuenciaLetra == 400:
            texto = texto + "P"
        elif frecuenciaLetra == 760:
            texto = texto + "Q"
        elif frecuenciaLetra == 1120:
            texto = texto + "R"
        elif frecuenciaLetra == 440:
            texto = texto + "S"
        elif frecuenciaLetra == 800:
            texto = texto + "T"
        elif frecuenciaLetra == 1160:
            texto = texto + "U"
        elif frecuenciaLetra == 480:
            texto = texto + "V"
        elif frecuenciaLetra == 840:
            texto = texto + "W"
        elif frecuenciaLetra == 1200:
            texto = texto + "X"
        elif frecuenciaLetra == 520:
            texto = texto + "Y"
        elif frecuenciaLetra == 880:
            texto = texto + "Z"
        else:
            texto = texto + "-"

    strSecuencia.set(texto)

    figure = Figure(figsize = (5,3), dpi = 100)
    figure.add_subplot(111).plot(waveTexto.ts, waveTexto.ys)
    canvas = FigureCanvasTkAgg(figure, master = principal)
    canvas.draw()
    canvas.get_tk_widget().pack()


strSecuencia = StringVar()
strSecuencia.set("Número contenido en el audio")

btnAbrir = Button(principal, text="Abrir ubicacion archivo wav", command = abrirArchivo)
btnAbrir.pack()

btnAnalisis = Button(principal, text="Analisis archivo wav", command = analizarArchivo)
btnAnalisis.pack()

lblarchivo = Label(principal, textvariable = strDirArchivo)
lblarchivo.pack()

lblarchivo = Label(principal, textvariable = strDireccionArchivo)
lblarchivo.pack()

lblarchivo = Label(principal, textvariable = strResultado)
lblarchivo.pack()

lblSecuenciaNumeros = Label(principal, textvariable = strSecuencia)
lblSecuenciaNumeros.pack()

mainloop()