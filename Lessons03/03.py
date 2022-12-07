num = abs(int(input("Введите число: ")))
suma_num = 0
mult_num = 1

while num > 0:
    a = num % 10
    suma_num += a
    mult_num *= a
    num = num // 10


print(f"Сумма: {suma_num}")
print(f"Произведение: {mult_num}")