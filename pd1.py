import numpy as np
from scipy.io.wavfile import write

sps = 44100
freq_hz = 440.0
duration = 0.1
vol = 0.3

# Большая_октава
d1 = [65.41, 73.91, 82.41, 87.31, 92.5, 98.0, 103.8, 110.0, 116.54, 123.48]

#Малая октава
d2 = []

# Первая октава

d3 =[]

# Вторая октава
d4 =[]

for j in range (10):
    a= d1[j]*2
    d2.append(a)
print(d2)


for j in range (10):
    a= d2[j]*2
    d3.append(a)
print(d3)

for j in range (10):
    a= d3[j]*2
    d4.append(a)
print(d4)



s="31415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 216420198"

print(len(s))
for i in range(len(s)):
    if s[i]=="0":
        h=d2[0]        
    elif s[i]== "1":
        h=d2[1]        
    elif s[i]== "2":
        h=d2[2]
        
    elif s[i]== "3":
        h=d2[3]       
        
    elif s[i]== "4":
        h=d2[4]
        
    elif s[i]== "5":
        h=d2[5]
        
    elif s[i]== "6":
        h=d2[6]
        
    elif s[i]== "7":
        h=d2[7]
        
    elif s[i]== "8":
        h=d2[8]        
        
    elif s[i]== "9":
        h=d2[9]
        
    esm = np.arange(duration * sps)
    
    wf = np.sin(2 * np.pi * esm * h / sps)

    wf_quiet = wf * vol
    wf_int = np.int16(wf_quiet * 32767)
    print(wf_int)
    t = "sample"+str(i)+".wav"
    
    write(t, sps, wf_int)   
       
        