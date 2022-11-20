import wave
#- The sample rate is 44100Hz
#- The increment size is 20

sound = wave.open('challenge2.wav', mode='rb')

x = sound.getparams()
frame_l = 1111280/20
frame=0
cur_frame=0
split = []
for i in range(20):
    frame += frame_l

    cur_frame = frame_l*i
    #sound.setpos(cur_frame)
    sec = sound.readframes(int(frame))
    split.append(sec)

sound.close()
print(split)
