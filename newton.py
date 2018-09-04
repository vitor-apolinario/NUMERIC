def f(x):
    return (x**3)-5

def f1(x):
    return (3*(x**2))

def f2(x):
    return (6*x)

a = int(input('A:'))
b = int(input('B:'))
e = 0.000001
it = 0

if f1(a)*f2(a) > 0:
    xn = float(b)
else:
    xn = float(a)

while True:
    xn = float(xn-(f(xn)/f1(xn)))
    it += 1
    print('xn:{} it:{}'.format(xn, it))
    if abs(f(xn))<e:
        break

print('root:{} it:{}'.format(xn, it))

