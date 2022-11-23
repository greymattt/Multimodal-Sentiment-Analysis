import numpy as np
import wave
# import matplotlib.pyplot as plt
# import scipy.integrate as integrate
wav_file = wave.open('audio.wav', 'r')
nchannels,sampwidth,framerate,nframes,comptype,compname = wav_file.getparams()
data = wav_file.readframes(nframes)
wav_file.close()
print(data)
