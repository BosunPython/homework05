from random import randint
n = 0
bot_num = randint(1, 20)
print("Привет. Играем в игру угадай число")
while True:
    player_num = input("Введите целое число от 1 до 20: ")
    n+=1
    if bot_num < player_num:
        print("Твое число больше")
    if bot_num > player_num:
        print("Твое число меньше")
    if bot_num == player_num:
        print("Ты угадал число!", "Робот загадал: ", bot_num, f"Ты угадал за {n}")
        break
