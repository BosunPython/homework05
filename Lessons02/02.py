num = int(input("Введите десятичное число: "))
con = input("Выберите численную систему: BIN, OCT, HEX ")
if con == "BIN":
    print("(Десятичная)", num, "=>", format(num, 'b'), "(Двоичная)")
elif con == "OCT":
    print("(Десятичная)", num, "=>", format(num, 'o'), "(Восьмеричная)")
elif con == "HEX":
    print("(Десятичная)", num, "=>", format(num, 'x'), "(Шестнадцатеричная)")
