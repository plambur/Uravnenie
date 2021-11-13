print('Выберите параметры для квадратного уравнения  ax^2+bx+c=0, чтобы определить его корни.')

a = int(input('Параметр а ='))
b = int(input('Параметр b ='))
c = int(input('Параметр c ='))

# print(str(a), 'x^2 +', str(b), 'x +', str(c), ' = 0 ')
print('%dx^2 + %dx + %d = 0' % (a,  b,  c) )


Discriminant = b * b - 4 * a * c

if Discriminant < 0:
    print('Корней нет')

elif Discriminant == 0:
    print('Дискриминант D = %d Есть ровно один корень.' % Discriminant )
    x = -b / (2 * a)
    print('x =', x)

elif Discriminant > 0:
    print('Дискриминант D = %d Корней будет два' % Discriminant)
    x1 = (-b - Discriminant ** 0.5) / (2 * a)
    x2 = (-b + Discriminant ** 0.5) / (2 * a)
    print('x1 = ', x1, '\nx2 = ', x2)
