import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt

seno = SinSignal(freq=400, amp=1, offset=0)
segundo_seno = SinSignal(freq=5000, amp=1, offset=0)
h = SinSignal(freq=640, amp=1, offset=0)
o = SinSignal(freq=1080, amp=1, offset=0)
l = SinSignal(freq=1040, amp=1, offset=0)
a = SinSignal(freq=200, amp=1, offset=0)

wave_seno = seno.make_wave(duration=0.5, start=0, framerate=44100)
wave_segundo_seno = segundo_seno.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_h = h.make_wave(duration=0.5, start=1, framerate=44100)
wave_o = o.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_l = l.make_wave(duration=0.5, start=2, framerate=44100)
wave_a = a.make_wave(duration=0.5, start=2.5, framerate=44100)

resultante = wave_seno + wave_segundo_seno + wave_h + wave_o + wave_l + wave_a

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")

resultante.plot()

resultante.write("Hola.wav")

plt.show()