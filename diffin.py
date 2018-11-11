import math

n=3
x=2.1

vetx=[0, 1, 2, 3]
vety=[1, 2, 5, 4]

h=vetx[1]-vetx[0]
z=(x-vetx[0]) / h

def diffin(n,i):
    if n==0:
        return vety[i]
    else:
        return float(diffin(n-1, i+1) - diffin(n-1, i))

print('h: {}; z: {}'.format(h, z))

result=vety[0]
for i in range(1, n+1):
    print('\niter: ',i)
    parcela=(diffin(i,0)*z) / math.factorial(i)
    if i > 1:
        for j in range(1,i):
            print('({} - {})'.format(z,j),end=' * ')
            parcela*=(z-j)
        print()
    result+=parcela

print('\n',result)