import wave

def muz(t1,t2):
    infiles1 = [t1, t2]
    outfile = x1

    data= []
    for infile in infiles1:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    
    

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])

    output.close()
j=0
# Всего 1107 = 1106+1
for i in range (0, 1106,2):
    
    t1 = "sample_octa" + str(i)+".wav"
    t2 = "sample_octa" + str(i+1)+".wav"
    x1 = "sounds_octa" + str(j)+".wav"
    j=j+1
    muz(t1,t2)
j=0
s3="sample_octa1106.wav"
s5= "sounds_octa552.wav"
for i in range (0,552,2):
    
    t1 = "sounds_octa" + str(i)+".wav"
    t2 = "sounds_octa" + str(i+1)+".wav"
    x1 = "audy_octa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,276,2):
    
    t1 = "audy_octa" + str(i)+".wav"
    t2 = "audy_octa" + str(i+1)+".wav"
    x1 = "aaa_octa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1

j=0
for i in range (0, 138, 2):
    
    t1 = "aaa_octa" + str(i)+".wav"
    t2 = "aaa_octa" + str(i+1)+".wav"
    x1 = "bbb_octa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
s5= "bbb_octa68.wav"
j=0
for i in range (0,68,2):
    
    t1 = "bbb_octa" + str(i)+".wav"
    t2 = "bbb_octa" + str(i+1)+".wav"
    x1 = "ccc_octa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,34, 2):
    
    t1 = "ccc_octa" + str(i)+".wav"
    t2 = "ccc_octa" + str(i+1)+".wav"
    x1 = "fff_octa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1

s8="fff_octa16.wav"
j=0
for i in range (0,16,2):
    
    t1 = "fff_octa" + str(i)+".wav"
    t2 = "fff_octa" + str(i+1)+".wav"
    x1 = "kkk_octa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,8,2):
    
    t1 = "kkk_octa" + str(i)+".wav"
    t2 = "kkk_octa" + str(i+1)+".wav"
    x1 = "yyy_octa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,4,2):
    t1 = "yyy_octa" + str(i)+".wav"
    t2 = "yyy_octa" + str(i+1)+".wav"
    x1 = "yyy1_octa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
t1 = "yyy1_octa" + str(0)+".wav"
t2 = "yyy1_octa" + str(1)+".wav"
x1 = "music_octa" + str(0)+".wav"
muz(t1,t2)

t1 = "music_octa0.wav"
t2 = "fff_octa16.wav"
x1 = "music" + str(1)+".wav"
muz(t1,t2)

t1 = "music1.wav"
t2 = "bbb_octa68.wav"
x1 = "music" + str(2)+".wav"
muz(t1,t2)

t1 = "music2.wav"
t2 = "sounds_octa552.wav"
x1 = "music" + str(3)+".wav"
muz(t1,t2)

t1 = "music3.wav"
t2 = "sample_octa1106.wav"
x1 = "music_octa" + str(5)+".wav"
muz(t1,t2)
