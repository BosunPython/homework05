start = int(input("Введите число от : "))
end = int(input("Введите числа до: "))
def SumRange(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))
print(SumRange(start, end))
