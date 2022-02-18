# encoding: utf-8
import numpy as np
import wave
import struct
  
fname = '100-500-1000-8000hz.wav'
wf = wave.open(fname, 'w')
ch = 1
width = 2
samplerate = 32000
wf.setnchannels(ch)
wf.setsampwidth(width)
wf.setframerate(samplerate)
  
time = 3600
numsamples = time * samplerate
  
print( u"チャンネル数 = ", ch)
print( u"サンプル幅 (バイト数) = ", width)
print( u"サンプリングレート (Hz) =", samplerate)
print( u"サンプル数 =", numsamples)
print( u"録音時間 =", time)
  
# 信号データを作る
# 周波数 100,500,1000,8000 (Hz) の正弦波
freq = 500 # 周波数 freq を 500Hz にする
x=np.linspace(0, time, numsamples+1) # 0 ≦ t ≦ time を numsamples 等分
y=np.sin(2 * np.pi * freq * x)+ \
    np.sin(2 * np.pi * 2*freq * x)+ \
    np.sin(2 * np.pi * 16*freq * x)+ \
    np.sin(2 * np.pi * freq/5 * x)
   
y=np.rint(32767*y/max(abs(y))) # [-32767,32767] の範囲に収める
y=y.astype(np.int16) # 16 ビット整数に型変換する
y=y[0:numsamples] # numsamples 個のデータに打ち切る
  
# ndarray から bytes オブジェクトに変換
data=struct.pack("h" * numsamples , *y)
  
# データを書き出す
wf.writeframes(data)
wf.close()

