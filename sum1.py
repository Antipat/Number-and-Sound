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
# Всего 1099 = 1098 +1
for i in range (0, 1098,2):
    
    t1 = "sample" + str(i)+".wav"
    t2 = "sample" + str(i+1)+".wav"
    x1 = "sounds" + str(j)+".wav"
    j=j+1
    muz(t1,t2)
j=0
s3="sample1098.wav"
s5= "sounds549.wav"
for i in range (0,548,2):
    
    t1 = "sounds" + str(i)+".wav"
    t2 = "sounds" + str(i+1)+".wav"
    x1 = "audy" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,274,2):
    
    t1 = "audy" + str(i)+".wav"
    t2 = "audy" + str(i+1)+".wav"
    x1 = "aaa" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
s7="audy136.wav"
j=0
for i in range (0, 136, 2):
    
    t1 = "aaa" + str(i)+".wav"
    t2 = "aaa" + str(i+1)+".wav"
    x1 = "bbb" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,68,2):
    
    t1 = "bbb" + str(i)+".wav"
    t2 = "bbb" + str(i+1)+".wav"
    x1 = "ccc" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,34, 2):
    
    t1 = "ccc" + str(i)+".wav"
    t2 = "ccc" + str(i+1)+".wav"
    x1 = "fff" + str(j)+".wav"
    muz(t1,t2)
    j=j+1

s8="fff16.wav"
j=0
for i in range (0,16,2):
    
    t1 = "fff" + str(i)+".wav"
    t2 = "fff" + str(i+1)+".wav"
    x1 = "kkk" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,8,2):
    
    t1 = "kkk" + str(i)+".wav"
    t2 = "kkk" + str(i+1)+".wav"
    x1 = "yyy" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
j=0
for i in range (0,4,2):
    t1 = "kkk" + str(i)+".wav"
    t2 = "kkk" + str(i+1)+".wav"
    x1 = "yyy" + str(j)+".wav"
    muz(t1,t2)
    j=j+1
t1 = "yyy" + str(0)+".wav"
t2 = "yyy" + str(1)+".wav"
x1 = "music" + str(0)+".wav"
muz(t1,t2)

t1 = "music0.wav"
t2 = "fff16.wav"
x1 = "music" + str(1)+".wav"
muz(t1,t2)

t1 = "music1.wav"
t2 = "audy136.wav"
x1 = "music" + str(2)+".wav"
muz(t1,t2)

t1 = "music2.wav"
t2 = "sounds549.wav"
x1 = "music" + str(3)+".wav"
muz(t1,t2)

t1 = "music3.wav"
t2 = "sample1098.wav"
x1 = "music" + str(5)+".wav"
muz(t1,t2)
