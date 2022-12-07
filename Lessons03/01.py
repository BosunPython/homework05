numbers = [2, -6, 7, -7, -3, 5]
pos_numbers = list()
neg_numbers = list()

for i in numbers:
    if int(i) >= 0:
        pos_numbers.append(i)
    else:
        neg_numbers.append(i)

print(pos_numbers)
print(neg_numbers)
