from math import fabs
x = float(input("Введите число "))
y = float(input("Введите число "))
print((fabs(x)-fabs(y)/(1+fabs(x)*fabs(y))))