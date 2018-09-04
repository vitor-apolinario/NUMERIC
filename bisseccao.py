def f(x):
    return float((x ** 3) - 5)

a = int(input('A:'))
inia = a
b = int(input('B:'))
inib = b
e = 0.000001
it = 0

while True:
    it += 1
    xn = float((a + b) / 2)
    fxn = float(f(xn))
    print('xn:{} it:{}'.format(xn, it))
    if abs(fxn) < e:
        break
    else:
        if f(a) * fxn < 0:
            b = xn
        else:
            a = xn

print('root:{}, it:{}'.format(xn, it))
