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
    letra = ""
    espacio = ""
    divisor1 = 100.0
    divisor2 = 10000.0
    waveTexto = read_wave(direccionArchivo)

    #numero de Letras que tendrá la palabra
    primerSegmento = []
    primerSegmento.append(waveTexto.segment(start=0, duration=0.5))
    frecuenciaPrimerSegmento = [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0]
    tolerancia = 10

    for segmento in primerSegmento:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 199:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        frecuenciaNumeroLetras = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciaPrimerSegmento:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    frecuenciaNumeroLetras  = frecuenciaDTMF
        letra = frecuenciaNumeroLetras/divisor1 
        #if frecuenciaNumeroLetras  == 100:
            #letra =  100 / divisor1
        #elif frecuenciaNumeroLetras  == 200:
            #letra =  200 / divisor1
        #elif frecuenciaNumeroLetras  == 300:
            #letra =  300 / divisor1
        #elif frecuenciaNumeroLetras  == 400:
            #letra =  400 / divisor1
        #elif frecuenciaNumeroLetras  == 500:
            #letra =  500 / divisor1
        #elif frecuenciaNumeroLetras  == 600:
            #letra =  600 / divisor1
        #elif frecuenciaNumeroLetras  == 700:
            #letra =  700 / divisor1
        #elif frecuenciaNumeroLetras  == 800:
            #letra =  800 / divisor1
        #elif frecuenciaNumeroLetras  == 900:
            #letra =  900 / divisor1
        #elif frecuenciaNumeroLetras  == 1000:
            #letra =  1000 / divisor1
        #else:
            #letra = "-"
    print(letra)
    round(letra)
    #tamaño del segmento de cada letra
    segundoSegmento = []
    segundoSegmento.append(waveTexto.segment(start=0.5, duration=0.5))
    frecuenciaSegundoSegmento = [1000, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    tolerancia2 = 500

    for segmento in segundoSegmento:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 499:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        frecuenciaTamaño = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciaSegundoSegmento:
                if frecuencia > frecuenciaDTMF - tolerancia2 and frecuencia < frecuenciaDTMF + tolerancia2:
                    frecuenciaTamaño  = frecuenciaDTMF
        espacio = frecuenciaTamaño/divisor2
        #if frecuenciaTamaño  == 1000:
            #espacio =  1000 / divisor2
        #elif frecuenciaTamaño  == 2000:
            #espacio =  2000 / divisor2
        #elif frecuenciaTamaño  == 2500:
            #espacio =  2500 / divisor2
        #elif frecuenciaTamaño  == 3000:
            #espacio =  3000 / divisor2
        #elif frecuenciaTamaño  == 4000:
            #espacio =  4000 / divisor2
        #elif frecuenciaTamaño  == 5000:
            #espacio =  5000 / divisor2
        #elif frecuenciaTamaño  == 6000:
            #espacio =  6000 / divisor2
        #elif frecuenciaTamaño  == 7000:
            #espacio =  7000 / divisor2
        #elif frecuenciaTamaño  == 8000:
            #espacio =  8000 / divisor2
        #elif frecuenciaTamaño  == 9000:
            #espacio =  9000 / divisor2
        #elif frecuenciaTamaño  == 10000:
            #espacio =  10000 / divisor2
        #else:
            #espacio = "-"
    print(espacio)

    #decodificador de la palabra
    segmentoTexto = []
    float(i)
    for i in range(int(letra)):
        segmentoTexto.append(waveTexto.segment(start=1.0+i*float(espacio), duration=float(espacio)))

    frecuenciasLetrasDTMF = [200, 240, 280, 320, 360, 400, 440, 480, 520, 
    560, 600, 640, 680, 720, 760, 800, 840, 880, 
    920, 6960, 1000, 1040, 1080, 1120, 1160, 1200]

    tolerancia = 10

    for segmento in segmentoTexto:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 189:
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