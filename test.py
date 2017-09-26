import numpy as np
import numpy.fft as nf
#for a in range(0, 10):
#    if a%2 == 0:
#        print(repr(a))

f = open('test.txt','r+')
a = []
for i in range(0,326):
    a.append(f.readline())
#a.append(f.readline())
#print(a)


b = [c.replace('\r\n', '') for c in a]
#print(b)

b = map(float,b)
arr = np.fft.fft(b)
#print(arr)
for i in range(50,326):
    arr[i] = 0


arr = np.fft.ifft(arr)
#print(arr)

arr = np.real(arr)

f = open('output.txt', 'w+')
b = [f.writelines(str(int(c))+'\n') for c in arr]

f.close()
#arr = np.array([[1,2,3],[4,5,6]]) 
#arr = np.fft.fft(np.exp(2j*np.pi*np.arange(8)/8)) 

