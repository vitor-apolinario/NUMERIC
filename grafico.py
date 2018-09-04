import matplotlib.pyplot as plt

def f(x):
    return ((x**3)-5)

a=int(input('Digite a:'))
b=int(input('Digite b:'))

zeros=[]
x=[]
y=[]

for i in range(a,b):
    x.append(i)
    y.append(f(i))
    zeros.append(0)

plt.plot(x,y)
plt.plot(x,zeros)
plt.show()