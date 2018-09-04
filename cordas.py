def f(x):
    return (x**3)-5

a = int(input('A:'))
b = int(input('B:'))
e = 0.000001
it = 0

x1 = float(((a*f(b))-(b*f(a)))/(f(b)-f(a)))
xn = 0.0

while True:
    if f(x1)*f(a)> 0:
        xn = float(((xn*f(b))-(b*f(xn)))/(f(b)-f(xn)))
    else:
        xn = float(((a*f(xn))-(xn*f(a)))/(f(xn)-f(a)))
    it += 1
    print('xn:{} it:{}'.format(xn, it))
    if abs(f(xn))<e:
        break

print('root:{} it:{}'.format(xn, it))